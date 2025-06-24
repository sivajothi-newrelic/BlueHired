from django.db import models
from django.core.validators import FileExtensionValidator
from users.models import User, JobSeekerProfile
from jobs.models import Job
import uuid

class JobApplication(models.Model):
    APPLICATION_STATUS = (
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('shortlisted', 'Shortlisted'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('interviewed', 'Interviewed'),
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
        ('withdrawn', 'Withdrawn'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    job_seeker_profile = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE, related_name='applications')
    
    # Application Details
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(
        upload_to='application_resumes/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
    )
    additional_documents = models.FileField(
        upload_to='application_documents/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'])]
    )
    
    # Status and Tracking
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    # Employer Actions
    viewed_by_employer = models.BooleanField(default=False)
    viewed_at = models.DateTimeField(null=True, blank=True)
    employer_notes = models.TextField(blank=True, null=True)
    
    # Interview Details
    interview_scheduled_at = models.DateTimeField(null=True, blank=True)
    interview_location = models.CharField(max_length=200, blank=True, null=True)
    interview_notes = models.TextField(blank=True, null=True)
    
    # Feedback
    employer_feedback = models.TextField(blank=True, null=True)
    applicant_feedback = models.TextField(blank=True, null=True)
    rating_by_employer = models.PositiveIntegerField(null=True, blank=True)  # 1-5 scale
    
    def __str__(self):
        return f"{self.applicant.email} applied for {self.job.title}"
    
    def save(self, *args, **kwargs):
        # Update job applications count
        if not self.pk:  # New application
            self.job.applications_count += 1
            self.job.save(update_fields=['applications_count'])
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'job_applications'
        unique_together = ['job', 'applicant']
        ordering = ['-applied_at']


class ApplicationStatusHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='status_history')
    previous_status = models.CharField(max_length=20, choices=JobApplication.APPLICATION_STATUS)
    new_status = models.CharField(max_length=20, choices=JobApplication.APPLICATION_STATUS)
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='status_changes')
    notes = models.TextField(blank=True, null=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.application.applicant.email} - {self.previous_status} to {self.new_status}"
    
    class Meta:
        db_table = 'application_status_history'
        ordering = ['-changed_at']


class Interview(models.Model):
    INTERVIEW_TYPES = (
        ('phone', 'Phone Interview'),
        ('video', 'Video Interview'),
        ('in_person', 'In-Person Interview'),
        ('group', 'Group Interview'),
        ('technical', 'Technical Interview'),
    )
    
    INTERVIEW_STATUS = (
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('rescheduled', 'Rescheduled'),
        ('no_show', 'No Show'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='interviews')
    interview_type = models.CharField(max_length=15, choices=INTERVIEW_TYPES, default='in_person')
    
    # Scheduling
    scheduled_at = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=30)
    location = models.CharField(max_length=200, blank=True, null=True)
    meeting_link = models.URLField(blank=True, null=True)  # For video interviews
    
    # Participants
    interviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conducted_interviews')
    additional_interviewers = models.ManyToManyField(User, blank=True, related_name='participated_interviews')
    
    # Status and Notes
    status = models.CharField(max_length=15, choices=INTERVIEW_STATUS, default='scheduled')
    preparation_notes = models.TextField(blank=True, null=True)
    interview_notes = models.TextField(blank=True, null=True)
    
    # Feedback
    technical_rating = models.PositiveIntegerField(null=True, blank=True)  # 1-5 scale
    communication_rating = models.PositiveIntegerField(null=True, blank=True)  # 1-5 scale
    overall_rating = models.PositiveIntegerField(null=True, blank=True)  # 1-5 scale
    recommendation = models.CharField(
        max_length=20,
        choices=[
            ('strongly_recommend', 'Strongly Recommend'),
            ('recommend', 'Recommend'),
            ('neutral', 'Neutral'),
            ('not_recommend', 'Not Recommend'),
            ('strongly_not_recommend', 'Strongly Not Recommend'),
        ],
        blank=True,
        null=True
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Interview for {self.application.applicant.email} - {self.application.job.title}"
    
    class Meta:
        db_table = 'interviews'
        ordering = ['-scheduled_at']


class ApplicationMessage(models.Model):
    MESSAGE_TYPES = (
        ('general', 'General'),
        ('interview_invite', 'Interview Invitation'),
        ('status_update', 'Status Update'),
        ('rejection', 'Rejection'),
        ('offer', 'Job Offer'),
        ('follow_up', 'Follow Up'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_application_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_application_messages')
    
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPES, default='general')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    # Attachments
    attachment = models.FileField(
        upload_to='application_message_attachments/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'])]
    )
    
    # Status
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    
    # Timestamps
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.sender.email} to {self.recipient.email}"
    
    class Meta:
        db_table = 'application_messages'
        ordering = ['-sent_at']


class JobOffer(models.Model):
    OFFER_STATUS = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('negotiating', 'Negotiating'),
        ('expired', 'Expired'),
        ('withdrawn', 'Withdrawn'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.OneToOneField(JobApplication, on_delete=models.CASCADE, related_name='job_offer')
    
    # Offer Details
    position_title = models.CharField(max_length=200)
    salary_offered = models.DecimalField(max_digits=10, decimal_places=2)
    salary_type = models.CharField(max_length=10, choices=[
        ('hourly', 'Per Hour'),
        ('daily', 'Per Day'),
        ('weekly', 'Per Week'),
        ('monthly', 'Per Month'),
        ('yearly', 'Per Year'),
        ('project', 'Per Project'),
    ], default='monthly')
    benefits = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    
    # Terms
    probation_period_months = models.PositiveIntegerField(default=3)
    notice_period_days = models.PositiveIntegerField(default=30)
    work_hours = models.CharField(max_length=100, blank=True, null=True)
    additional_terms = models.TextField(blank=True, null=True)
    
    # Status and Dates
    status = models.CharField(max_length=15, choices=OFFER_STATUS, default='pending')
    offer_valid_until = models.DateTimeField()
    offered_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(null=True, blank=True)
    
    # Documents
    offer_letter = models.FileField(
        upload_to='offer_letters/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    
    # Response
    candidate_response = models.TextField(blank=True, null=True)
    counter_offer_details = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Offer for {self.application.applicant.email} - {self.position_title}"
    
    class Meta:
        db_table = 'job_offers'
        ordering = ['-offered_at']


class ApplicationFeedback(models.Model):
    FEEDBACK_TYPES = (
        ('employer_to_candidate', 'Employer to Candidate'),
        ('candidate_to_employer', 'Candidate to Employer'),
        ('platform_feedback', 'Platform Feedback'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='feedback')
    feedback_type = models.CharField(max_length=25, choices=FEEDBACK_TYPES)
    given_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_feedback')
    
    # Ratings (1-5 scale)
    overall_rating = models.PositiveIntegerField(null=True, blank=True)
    communication_rating = models.PositiveIntegerField(null=True, blank=True)
    professionalism_rating = models.PositiveIntegerField(null=True, blank=True)
    
    # Comments
    positive_feedback = models.TextField(blank=True, null=True)
    areas_for_improvement = models.TextField(blank=True, null=True)
    additional_comments = models.TextField(blank=True, null=True)
    
    # Recommendations
    would_recommend = models.BooleanField(null=True, blank=True)
    would_work_again = models.BooleanField(null=True, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Feedback for {self.application.applicant.email} by {self.given_by.email}"
    
    class Meta:
        db_table = 'application_feedback'
        unique_together = ['application', 'given_by', 'feedback_type']
        ordering = ['-created_at']
