# BlueHired - Blue Collar Job Listings Platform

A comprehensive job portal specifically designed for blue-collar workers, connecting job seekers with employers in various industries including construction, manufacturing, transportation, hospitality, and more.

## 🚀 Features

### For Job Seekers
- **Government ID Verification**: Secure verification using Aadhaar, PAN, Driving License, Voter ID, or Passport
- **Advanced Job Search**: Filter by location, skills, experience level, and salary range
- **Profile Management**: Complete profile with skills, experience, and resume upload
- **Job Applications**: Apply to jobs with cover letters and additional documents
- **Application Tracking**: Track application status and receive updates
- **Job Alerts**: Set up custom alerts for relevant job opportunities
- **Bookmarks**: Save interesting job listings for later

### For Job Posters/Employers
- **Company Verification**: Verified company profiles with detailed information
- **Job Posting**: Create detailed job listings with requirements and benefits
- **Application Management**: Review applications, schedule interviews, and manage hiring process
- **Candidate Communication**: Direct messaging with applicants
- **Interview Scheduling**: Built-in interview management system
- **Offer Management**: Send job offers and track responses

### Platform Features
- **Role-based Access Control**: Separate interfaces for job seekers and employers
- **Material-UI Design**: Clean, modern, and mobile-responsive interface
- **Real-time Notifications**: Stay updated on application status and new opportunities
- **Advanced Analytics**: Job view tracking and application metrics
- **Reporting System**: Report inappropriate content or fake job listings

## 🛠 Technology Stack

### Backend
- **Django 4.2.23**: Python web framework
- **Django REST Framework**: API development
- **JWT Authentication**: Secure token-based authentication
- **PostgreSQL**: Production database (SQLite for development)
- **Python Decouple**: Environment configuration management

### Frontend (Planned)
- **React.js**: Modern JavaScript framework
- **Material-UI**: Google's Material Design components
- **Redux Toolkit**: State management
- **Axios**: HTTP client for API calls

### Infrastructure
- **AWS**: Cloud deployment platform
- **Docker**: Containerization
- **GitHub Actions**: CI/CD pipeline

## 📋 Prerequisites

- Python 3.9+
- Node.js 16+ (for frontend)
- PostgreSQL (for production)
- Git

## 🚀 Quick Start

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone git@source.datanerd.us:naveenkumar/BlueHired.git
   cd BlueHired
   ```

2. **Set up Python virtual environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the backend directory:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DB_NAME=blue_collar_jobs
   DB_USER=postgres
   DB_PASSWORD=your-password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

### Frontend Setup (Coming Soon)

```bash
cd frontend
npm install
npm start
```

## 📊 Database Schema

### Core Models

#### User Management
- **User**: Extended Django user with role-based access
- **VerificationDocument**: Government ID verification system
- **JobSeekerProfile**: Job seeker specific information
- **JobPosterProfile**: Employer/company information
- **Skill**: Skills database with categories

#### Job Management
- **JobCategory**: Job categories (Construction, Manufacturing, etc.)
- **Job**: Job listings with detailed requirements
- **JobSkillRequirement**: Required skills for jobs
- **JobBookmark**: Saved jobs by users
- **JobAlert**: Custom job alerts
- **JobView**: Job view tracking

#### Application Management
- **JobApplication**: Job applications with status tracking
- **ApplicationStatusHistory**: Application status change history
- **Interview**: Interview scheduling and management
- **ApplicationMessage**: Communication between employers and candidates
- **JobOffer**: Job offer management
- **ApplicationFeedback**: Feedback system

## 🔐 Authentication & Security

- JWT-based authentication with refresh tokens
- Role-based access control (Job Seeker, Job Poster, Admin)
- Government ID verification for user authenticity
- File upload validation and security
- CORS configuration for frontend integration
- Secure password validation

## 📱 API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/refresh/` - Token refresh
- `POST /api/auth/logout/` - User logout

### User Management
- `GET /api/users/profile/` - Get user profile
- `PUT /api/users/profile/` - Update user profile
- `POST /api/users/verify/` - Upload verification documents

### Jobs
- `GET /api/jobs/` - List jobs with filters
- `POST /api/jobs/` - Create job (employers only)
- `GET /api/jobs/{id}/` - Job details
- `PUT /api/jobs/{id}/` - Update job
- `DELETE /api/jobs/{id}/` - Delete job

### Applications
- `POST /api/applications/` - Apply for job
- `GET /api/applications/` - List user applications
- `PUT /api/applications/{id}/` - Update application status

## 🌟 Key Features Implementation

### Government ID Verification
- Support for multiple Indian government IDs
- OCR text extraction for automatic validation
- Admin review workflow for complex cases
- Verification status tracking

### Advanced Job Search
- Location-based filtering
- Skills matching algorithm
- Experience level filtering
- Salary range filtering
- Job type and category filters

### Application Management
- Complete application lifecycle tracking
- Interview scheduling system
- Offer management with negotiation support
- Communication system between parties

## 🚀 Deployment

### AWS Deployment Architecture
- **Frontend**: S3 + CloudFront
- **Backend**: ECS Fargate or EC2
- **Database**: RDS PostgreSQL
- **File Storage**: S3 buckets
- **CDN**: CloudFront for global delivery
- **Email**: SES for notifications

### Environment Variables
```env
# Production settings
DEBUG=False
ALLOWED_HOSTS=your-domain.com
SECRET_KEY=your-production-secret-key

# Database
DB_NAME=bluehired_prod
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=your-rds-endpoint
DB_PORT=5432

# AWS Settings
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=your-s3-bucket
AWS_S3_REGION_NAME=your-region

# Email
EMAIL_HOST=your-smtp-host
EMAIL_PORT=587
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-email-password
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **Development Team**: Building the future of blue-collar employment
- **Contact**: [Your contact information]

## 🔮 Roadmap

### Phase 1 (Current)
- ✅ Backend API development
- ✅ User authentication and verification
- ✅ Job management system
- ✅ Application management

### Phase 2 (Next)
- 🔄 React.js frontend development
- 🔄 Material-UI implementation
- 🔄 API integration
- 🔄 User testing

### Phase 3 (Future)
- 📱 Mobile app development
- 🤖 AI-powered job matching
- 📊 Advanced analytics dashboard
- 🌐 Multi-language support

## 📞 Support

For support, email support@bluehired.com or create an issue in this repository.

---

**BlueHired** - Connecting blue-collar workers with opportunities, one job at a time. 🔧⚡🏗️
