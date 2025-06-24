from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime, timedelta
import random

from users.models import JobSeekerProfile, JobPosterProfile, Skill, JobSeekerSkill
from jobs.models import JobCategory, Job, JobSkillRequirement
from applications.models import JobApplication

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the database with sample job listings and job seeker records'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🚀 Starting to populate sample data...'))
        
        # Create job categories
        self.create_job_categories()
        
        # Create skills
        self.create_skills()
        
        # Create job seekers
        self.create_job_seekers()
        
        # Create job posters (employers)
        self.create_job_posters()
        
        # Create job listings
        self.create_job_listings()
        
        # Create some applications
        self.create_applications()
        
        self.stdout.write(self.style.SUCCESS('✅ Sample data population completed!'))

    def create_job_categories(self):
        self.stdout.write('📂 Creating job categories...')
        
        categories = [
            {
                'name': 'Construction',
                'description': 'Building, renovation, and construction work',
                'icon': 'construction'
            },
            {
                'name': 'Manufacturing',
                'description': 'Factory work, assembly, and production',
                'icon': 'factory'
            },
            {
                'name': 'Transportation',
                'description': 'Driving, delivery, and logistics',
                'icon': 'truck'
            },
            {
                'name': 'Hospitality',
                'description': 'Hotels, restaurants, and food service',
                'icon': 'restaurant'
            },
            {
                'name': 'Maintenance',
                'description': 'Repair, cleaning, and facility maintenance',
                'icon': 'tools'
            },
            {
                'name': 'Security',
                'description': 'Security guards and safety personnel',
                'icon': 'security'
            },
            {
                'name': 'Retail',
                'description': 'Sales, customer service, and retail operations',
                'icon': 'store'
            },
            {
                'name': 'Healthcare Support',
                'description': 'Healthcare assistants and support staff',
                'icon': 'medical'
            }
        ]
        
        for cat_data in categories:
            category, created = JobCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'description': cat_data['description'],
                    'icon': cat_data['icon'],
                    'is_active': True
                }
            )
            if created:
                self.stdout.write(f'  ✓ Created category: {category.name}')

    def create_skills(self):
        self.stdout.write('🛠️ Creating skills...')
        
        skills_data = [
            # Construction Skills
            ('Carpentry', 'construction'),
            ('Plumbing', 'construction'),
            ('Electrical Work', 'construction'),
            ('Welding', 'construction'),
            ('Masonry', 'construction'),
            ('Painting', 'construction'),
            ('Roofing', 'construction'),
            ('Heavy Equipment Operation', 'construction'),
            
            # Manufacturing Skills
            ('Assembly Line Work', 'manufacturing'),
            ('Quality Control', 'manufacturing'),
            ('Machine Operation', 'manufacturing'),
            ('Packaging', 'manufacturing'),
            ('Inventory Management', 'manufacturing'),
            ('Forklift Operation', 'manufacturing'),
            
            # Transportation Skills
            ('Commercial Driving', 'transportation'),
            ('Delivery Services', 'transportation'),
            ('Vehicle Maintenance', 'transportation'),
            ('Route Planning', 'transportation'),
            ('Loading/Unloading', 'transportation'),
            
            # Hospitality Skills
            ('Food Preparation', 'hospitality'),
            ('Customer Service', 'hospitality'),
            ('Cleaning', 'hospitality'),
            ('Cash Handling', 'hospitality'),
            ('Food Safety', 'hospitality'),
            
            # Maintenance Skills
            ('HVAC Repair', 'maintenance'),
            ('Janitorial Services', 'maintenance'),
            ('Landscaping', 'maintenance'),
            ('Equipment Repair', 'maintenance'),
            
            # Security Skills
            ('Security Monitoring', 'security'),
            ('Access Control', 'security'),
            ('Emergency Response', 'security'),
            
            # General Skills
            ('Physical Fitness', 'general'),
            ('Team Work', 'general'),
            ('Time Management', 'general'),
            ('Communication', 'general'),
            ('Problem Solving', 'general'),
            ('Safety Compliance', 'general')
        ]
        
        for skill_name, category in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_name,
                defaults={
                    'category': category,
                    'description': f'Professional skill in {skill_name.lower()}',
                    'is_active': True
                }
            )
            if created:
                self.stdout.write(f'  ✓ Created skill: {skill.name}')

    def create_job_seekers(self):
        self.stdout.write('👷 Creating job seekers...')
        
        job_seekers_data = [
            {
                'email': 'rajesh.kumar@email.com',
                'first_name': 'Rajesh',
                'last_name': 'Kumar',
                'phone': '+91-9876543210',
                'city': 'Mumbai',
                'state': 'Maharashtra',
                'experience_years': 5,
                'skills': ['Carpentry', 'Painting', 'Safety Compliance']
            },
            {
                'email': 'priya.sharma@email.com',
                'first_name': 'Priya',
                'last_name': 'Sharma',
                'phone': '+91-9876543211',
                'city': 'Delhi',
                'state': 'Delhi',
                'experience_years': 3,
                'skills': ['Customer Service', 'Cash Handling', 'Food Safety']
            },
            {
                'email': 'amit.singh@email.com',
                'first_name': 'Amit',
                'last_name': 'Singh',
                'phone': '+91-9876543212',
                'city': 'Bangalore',
                'state': 'Karnataka',
                'experience_years': 7,
                'skills': ['Commercial Driving', 'Vehicle Maintenance', 'Route Planning']
            },
            {
                'email': 'sunita.devi@email.com',
                'first_name': 'Sunita',
                'last_name': 'Devi',
                'phone': '+91-9876543213',
                'city': 'Chennai',
                'state': 'Tamil Nadu',
                'experience_years': 2,
                'skills': ['Cleaning', 'Janitorial Services', 'Time Management']
            },
            {
                'email': 'ravi.patel@email.com',
                'first_name': 'Ravi',
                'last_name': 'Patel',
                'phone': '+91-9876543214',
                'city': 'Ahmedabad',
                'state': 'Gujarat',
                'experience_years': 8,
                'skills': ['Welding', 'Heavy Equipment Operation', 'Safety Compliance']
            },
            {
                'email': 'meera.joshi@email.com',
                'first_name': 'Meera',
                'last_name': 'Joshi',
                'phone': '+91-9876543215',
                'city': 'Pune',
                'state': 'Maharashtra',
                'experience_years': 4,
                'skills': ['Assembly Line Work', 'Quality Control', 'Team Work']
            },
            {
                'email': 'vikram.yadav@email.com',
                'first_name': 'Vikram',
                'last_name': 'Yadav',
                'phone': '+91-9876543216',
                'city': 'Hyderabad',
                'state': 'Telangana',
                'experience_years': 6,
                'skills': ['Security Monitoring', 'Emergency Response', 'Communication']
            },
            {
                'email': 'kavita.reddy@email.com',
                'first_name': 'Kavita',
                'last_name': 'Reddy',
                'phone': '+91-9876543217',
                'city': 'Kolkata',
                'state': 'West Bengal',
                'experience_years': 3,
                'skills': ['Food Preparation', 'Customer Service', 'Food Safety']
            }
        ]
        
        for seeker_data in job_seekers_data:
            # Create user
            user, created = User.objects.get_or_create(
                email=seeker_data['email'],
                defaults={
                    'username': seeker_data['email'],
                    'first_name': seeker_data['first_name'],
                    'last_name': seeker_data['last_name'],
                    'role': 'job_seeker',
                    'is_active': True,
                    'is_verified': True
                }
            )
            
            if created:
                user.set_password('password123')
                user.save()
                
                # Create job seeker profile
                experience_level = 'entry'
                if seeker_data['experience_years'] >= 10:
                    experience_level = 'expert'
                elif seeker_data['experience_years'] >= 5:
                    experience_level = 'senior'
                elif seeker_data['experience_years'] >= 2:
                    experience_level = 'mid'
                
                profile = JobSeekerProfile.objects.create(
                    user=user,
                    bio=f"Experienced {seeker_data['first_name']} with {seeker_data['experience_years']} years in the field.",
                    experience_level=experience_level,
                    location=f"{seeker_data['city']}, {seeker_data['state']}",
                    city=seeker_data['city'],
                    state=seeker_data['state'],
                    pincode=f"{random.randint(100000, 999999)}",
                    availability=True,
                    expected_salary_min=random.randint(15000, 40000),
                    expected_salary_max=random.randint(25000, 60000)
                )
                
                # Set phone number on user
                user.phone_number = seeker_data['phone']
                user.save()
                
                # Add skills
                for skill_name in seeker_data['skills']:
                    try:
                        skill = Skill.objects.get(name=skill_name)
                        JobSeekerSkill.objects.create(
                            job_seeker=profile,
                            skill=skill,
                            proficiency_level='intermediate',
                            years_of_experience=random.randint(1, seeker_data['experience_years'])
                        )
                    except Skill.DoesNotExist:
                        pass
                
                self.stdout.write(f'  ✓ Created job seeker: {user.get_full_name()}')

    def create_job_posters(self):
        self.stdout.write('🏢 Creating job posters (employers)...')
        
        employers_data = [
            {
                'email': 'hr@constructionplus.com',
                'first_name': 'Suresh',
                'last_name': 'Agarwal',
                'company_name': 'Construction Plus Pvt Ltd',
                'company_type': 'construction',
                'city': 'Mumbai',
                'state': 'Maharashtra'
            },
            {
                'email': 'jobs@quickdelivery.com',
                'first_name': 'Anita',
                'last_name': 'Gupta',
                'company_name': 'Quick Delivery Services',
                'company_type': 'logistics',
                'city': 'Delhi',
                'state': 'Delhi'
            },
            {
                'email': 'careers@techmanufacturing.com',
                'first_name': 'Ramesh',
                'last_name': 'Iyer',
                'company_name': 'Tech Manufacturing Ltd',
                'company_type': 'manufacturing',
                'city': 'Bangalore',
                'state': 'Karnataka'
            },
            {
                'email': 'hiring@grandhotel.com',
                'first_name': 'Deepa',
                'last_name': 'Nair',
                'company_name': 'Grand Hotel & Resorts',
                'company_type': 'hospitality',
                'city': 'Chennai',
                'state': 'Tamil Nadu'
            },
            {
                'email': 'recruitment@securitypro.com',
                'first_name': 'Manoj',
                'last_name': 'Thakur',
                'company_name': 'Security Pro Services',
                'company_type': 'security',
                'city': 'Pune',
                'state': 'Maharashtra'
            }
        ]
        
        for employer_data in employers_data:
            # Create user
            user, created = User.objects.get_or_create(
                email=employer_data['email'],
                defaults={
                    'username': employer_data['email'],
                    'first_name': employer_data['first_name'],
                    'last_name': employer_data['last_name'],
                    'role': 'job_poster',
                    'is_active': True,
                    'is_verified': True
                }
            )
            
            if created:
                user.set_password('password123')
                user.save()
                
                # Create job poster profile
                JobPosterProfile.objects.create(
                    user=user,
                    company_name=employer_data['company_name'],
                    company_size='medium',
                    industry=employer_data['company_type'],
                    company_description=f"{employer_data['company_name']} is a leading company in {employer_data['company_type']} sector.",
                    website=f"https://www.{employer_data['company_name'].lower().replace(' ', '').replace('&', '').replace('ltd', '').replace('pvt', '')}.com",
                    contact_phone=f"+91-{random.randint(1000000000, 9999999999)}",
                    address=f"Corporate Office, {employer_data['city']}",
                    city=employer_data['city'],
                    state=employer_data['state'],
                    pincode=f"{random.randint(100000, 999999)}",
                    is_company_verified=True
                )
                
                self.stdout.write(f'  ✓ Created employer: {employer_data["company_name"]}')

    def create_job_listings(self):
        self.stdout.write('💼 Creating job listings...')
        
        jobs_data = [
            {
                'title': 'Construction Worker - Residential Projects',
                'category': 'Construction',
                'company_email': 'hr@constructionplus.com',
                'description': 'We are looking for experienced construction workers for residential building projects. Must have experience in carpentry, painting, and general construction work.',
                'requirements': 'Minimum 2 years experience in construction, Physical fitness required, Safety certification preferred',
                'location': 'Mumbai, Maharashtra',
                'salary_min': 25000,
                'salary_max': 35000,
                'job_type': 'full_time',
                'experience_required': 2,
                'skills': ['Carpentry', 'Painting', 'Safety Compliance']
            },
            {
                'title': 'Delivery Driver - Two Wheeler',
                'category': 'Transportation',
                'company_email': 'jobs@quickdelivery.com',
                'description': 'Join our delivery team! We need reliable drivers with their own two-wheeler for food and package delivery across Delhi NCR.',
                'requirements': 'Valid driving license, Own two-wheeler, Good knowledge of Delhi roads, Smartphone required',
                'location': 'Delhi, Delhi',
                'salary_min': 20000,
                'salary_max': 30000,
                'job_type': 'full_time',
                'experience_required': 1,
                'skills': ['Commercial Driving', 'Route Planning', 'Customer Service']
            },
            {
                'title': 'Production Line Operator',
                'category': 'Manufacturing',
                'company_email': 'careers@techmanufacturing.com',
                'description': 'Operate production machinery and ensure quality standards in our electronics manufacturing facility. Training will be provided.',
                'requirements': '12th pass minimum, Willingness to work in shifts, Basic technical aptitude, Team player',
                'location': 'Bangalore, Karnataka',
                'salary_min': 18000,
                'salary_max': 25000,
                'job_type': 'full_time',
                'experience_required': 0,
                'skills': ['Assembly Line Work', 'Quality Control', 'Machine Operation']
            },
            {
                'title': 'Hotel Housekeeping Staff',
                'category': 'Hospitality',
                'company_email': 'hiring@grandhotel.com',
                'description': 'Maintain cleanliness and hygiene standards in our 5-star hotel. Experience in hospitality sector preferred.',
                'requirements': 'Previous housekeeping experience, Attention to detail, Physical stamina, Good communication skills',
                'location': 'Chennai, Tamil Nadu',
                'salary_min': 15000,
                'salary_max': 22000,
                'job_type': 'full_time',
                'experience_required': 1,
                'skills': ['Cleaning', 'Customer Service', 'Time Management']
            },
            {
                'title': 'Security Guard - Night Shift',
                'category': 'Security',
                'company_email': 'recruitment@securitypro.com',
                'description': 'Provide security services for commercial buildings during night hours. Must be alert and responsible.',
                'requirements': 'Security training certificate, Physical fitness, No criminal background, Willing to work night shifts',
                'location': 'Pune, Maharashtra',
                'salary_min': 16000,
                'salary_max': 20000,
                'job_type': 'full_time',
                'experience_required': 1,
                'skills': ['Security Monitoring', 'Emergency Response', 'Communication']
            },
            {
                'title': 'Welder - Structural Steel',
                'category': 'Construction',
                'company_email': 'hr@constructionplus.com',
                'description': 'Experienced welder needed for structural steel work on commercial construction projects. Arc welding experience required.',
                'requirements': 'Certified welder, 3+ years experience, Ability to read blueprints, Safety conscious',
                'location': 'Mumbai, Maharashtra',
                'salary_min': 30000,
                'salary_max': 45000,
                'job_type': 'full_time',
                'experience_required': 3,
                'skills': ['Welding', 'Safety Compliance', 'Heavy Equipment Operation']
            },
            {
                'title': 'Restaurant Kitchen Helper',
                'category': 'Hospitality',
                'company_email': 'hiring@grandhotel.com',
                'description': 'Assist chefs in food preparation, maintain kitchen cleanliness, and support restaurant operations.',
                'requirements': 'Food handling knowledge, Willingness to work flexible hours, Team player, Basic English',
                'location': 'Chennai, Tamil Nadu',
                'salary_min': 12000,
                'salary_max': 18000,
                'job_type': 'full_time',
                'experience_required': 0,
                'skills': ['Food Preparation', 'Cleaning', 'Food Safety']
            },
            {
                'title': 'Forklift Operator',
                'category': 'Manufacturing',
                'company_email': 'careers@techmanufacturing.com',
                'description': 'Operate forklift for material handling in our warehouse. Forklift license required.',
                'requirements': 'Valid forklift license, 2+ years experience, Good spatial awareness, Safety focused',
                'location': 'Bangalore, Karnataka',
                'salary_min': 22000,
                'salary_max': 28000,
                'job_type': 'full_time',
                'experience_required': 2,
                'skills': ['Forklift Operation', 'Inventory Management', 'Safety Compliance']
            },
            {
                'title': 'Plumber - Residential & Commercial',
                'category': 'Maintenance',
                'company_email': 'hr@constructionplus.com',
                'description': 'Handle plumbing installations, repairs, and maintenance for residential and commercial properties.',
                'requirements': 'Plumbing certification, 3+ years experience, Own tools preferred, Problem-solving skills',
                'location': 'Mumbai, Maharashtra',
                'salary_min': 25000,
                'salary_max': 40000,
                'job_type': 'full_time',
                'experience_required': 3,
                'skills': ['Plumbing', 'Problem Solving', 'Customer Service']
            },
            {
                'title': 'Warehouse Packer',
                'category': 'Manufacturing',
                'company_email': 'careers@techmanufacturing.com',
                'description': 'Pack products according to specifications, maintain quality standards, and prepare shipments.',
                'requirements': 'Attention to detail, Physical stamina, Basic math skills, Reliable attendance',
                'location': 'Bangalore, Karnataka',
                'salary_min': 15000,
                'salary_max': 20000,
                'job_type': 'full_time',
                'experience_required': 0,
                'skills': ['Packaging', 'Quality Control', 'Time Management']
            }
        ]
        
        for job_data in jobs_data:
            try:
                # Get the job poster
                poster_user = User.objects.get(email=job_data['company_email'])
                poster_profile = JobPosterProfile.objects.get(user=poster_user)
                
                # Get the category
                category = JobCategory.objects.get(name=job_data['category'])
                
                # Map experience years to experience level
                experience_level = 'entry'
                if job_data['experience_required'] >= 10:
                    experience_level = 'expert'
                elif job_data['experience_required'] >= 5:
                    experience_level = 'senior'
                elif job_data['experience_required'] >= 2:
                    experience_level = 'mid'
                
                # Create the job
                job = Job.objects.create(
                    title=job_data['title'],
                    category=category,
                    company=poster_profile,
                    posted_by=poster_user,
                    description=job_data['description'],
                    requirements=job_data['requirements'],
                    location=job_data['location'],
                    city=job_data['location'].split(',')[0].strip(),
                    state=job_data['location'].split(',')[1].strip() if ',' in job_data['location'] else '',
                    salary_min=job_data['salary_min'],
                    salary_max=job_data['salary_max'],
                    salary_type='monthly',
                    job_type=job_data['job_type'],
                    experience_level=experience_level,
                    application_deadline=timezone.now() + timedelta(days=30),
                    status='active',
                    is_featured=random.choice([True, False])
                )
                
                # Add required skills
                for skill_name in job_data['skills']:
                    try:
                        skill = Skill.objects.get(name=skill_name)
                        JobSkillRequirement.objects.create(
                            job=job,
                            skill=skill,
                            requirement_level='required'
                        )
                    except Skill.DoesNotExist:
                        pass
                
                self.stdout.write(f'  ✓ Created job: {job.title}')
                
            except (User.DoesNotExist, JobPosterProfile.DoesNotExist, JobCategory.DoesNotExist):
                self.stdout.write(f'  ✗ Failed to create job: {job_data["title"]}')

    def create_applications(self):
        self.stdout.write('📝 Creating job applications...')
        
        # Get some job seekers and jobs
        job_seekers = list(JobSeekerProfile.objects.all()[:5])
        jobs = list(Job.objects.all()[:8])
        
        applications_created = 0
        
        for job_seeker in job_seekers:
            # Each job seeker applies to 2-3 random jobs
            num_applications = random.randint(2, 3)
            selected_jobs = random.sample(jobs, min(num_applications, len(jobs)))
            
            for job in selected_jobs:
                # Check if application already exists
                if not JobApplication.objects.filter(job=job, applicant=job_seeker.user).exists():
                    application = JobApplication.objects.create(
                        job=job,
                        applicant=job_seeker.user,
                        job_seeker_profile=job_seeker,
                        cover_letter=f"Dear Hiring Manager,\n\nI am interested in the {job.title} position at {job.company.company_name}. With my experience in {job_seeker.experience_level} level work, I believe I would be a great fit for this role.\n\nThank you for your consideration.\n\nBest regards,\n{job_seeker.user.get_full_name()}",
                        status=random.choice(['pending', 'under_review', 'shortlisted']),
                        applied_at=timezone.now() - timedelta(days=random.randint(1, 15))
                    )
                    applications_created += 1
                    
        self.stdout.write(f'  ✓ Created {applications_created} job applications')

    def print_summary(self):
        self.stdout.write('\n📊 Database Summary:')
        self.stdout.write(f'  • Job Categories: {JobCategory.objects.count()}')
        self.stdout.write(f'  • Skills: {Skill.objects.count()}')
        self.stdout.write(f'  • Job Seekers: {JobSeekerProfile.objects.count()}')
        self.stdout.write(f'  • Employers: {JobPosterProfile.objects.count()}')
        self.stdout.write(f'  • Job Listings: {Job.objects.count()}')
        self.stdout.write(f'  • Applications: {JobApplication.objects.count()}')
