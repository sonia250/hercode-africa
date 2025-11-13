# HerCode Africa

A mentorship and peer support platform for African women in technology.

## Project Overview

HerCode Africa is a web-based platform designed to bridge the gender gap in technology by connecting African women with mentors, resources, and supportive peer communities. The platform enables women to access quality programming education, find experienced mentors, and collaborate with peers in their learning journey.

## Problem Statement

African women face significant barriers when entering the technology sector, including:
- Lack of accessible mentorship opportunities
- Limited peer support networks
- Inadequate access to quality learning resources
- Underrepresentation in STEM fields (less than 30% globally, even lower in Africa)

## Solution

HerCode Africa provides:
- **Mentor Matching System**: Connect mentees with experienced technology professionals
- **Peer Learning Groups**: Join communities focused on specific programming topics
- **Tutorial Library**: Access curated programming tutorials from beginner to advanced
- **Progress Tracking**: Monitor learning achievements and completed courses
- **Admin Dashboard**: Manage users, content, and platform activities

## Features

### For Mentees
- Register and create personalized profiles
- Browse and request mentors based on expertise
- Join peer learning groups
- Access programming tutorials
- Track learning progress
- Receive notifications for sessions and updates

### For Mentors
- Share expertise with aspiring developers
- Accept mentorship requests
- Schedule and conduct mentoring sessions
- Provide feedback to mentees
- Join peer groups to offer guidance

### For Administrators
- Manage user accounts
- Add and moderate tutorials
- Oversee mentorship activities
- View platform analytics

## Technology Stack

- **Backend**: Django 5.2.8 (Python web framework)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production)
- **Authentication**: Django built-in authentication system
- **Deployment**: PythonAnywhere

## Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/hercode-africa.git
cd hercode-africa
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run Migrations
```bash
python manage.py migrate
```

### Step 6: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### Step 7: Run Development Server
```bash
python manage.py runserver
```

### Step 8: Access the Application
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
hercode-africa/
├── accounts/              # User authentication and profiles
├── mentorship/            # Mentor-mentee relationships and peer groups
├── tutorials/             # Learning resources and progress tracking
├── hercode_project/       # Project settings and configuration
├── templates/             # HTML templates
├── staticfiles/           # Static files (CSS, JS, images)
├── media/                 # User-uploaded files
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## Usage Guide

### Creating a Mentee Account
1. Navigate to the registration page
2. Fill in your details and select "Mentee" as user type
3. Complete your profile with learning interests
4. Browse available mentors and send requests

### Creating a Mentor Account
1. Register and select "Mentor" as user type
2. Add your expertise and availability
3. Review mentorship requests
4. Accept mentees and schedule sessions

### Using the Admin Panel
1. Access /admin/ with superuser credentials
2. Add tutorials, manage users, and oversee activities
3. Create peer groups and moderate content

## System Requirements (SRS)

For detailed system requirements, please refer to the SRS document which includes:
- Functional requirements (FR1-FR7)
- Non-functional requirements (NFR1-NFR7)
- UML diagrams (Class, Use Case, Sequence, Activity)
- System architecture and design constraints

## Contributing

This project was developed as part of the ALU Software Engineering curriculum.

## Author

**Mutesi Uwase Sonia**
- Institution: African Leadership University
- Project: HerCode Africa Mentorship Platform
- Date: November 2025

## License

This project is created for educational purposes.

## Acknowledgments

- ALU Faculty and Mentors
- All women in technology who inspired this project
- The Django and Bootstrap communities

## Contact

For questions or support, please contact through the platform's admin panel.

---

**Empowering African Women in Technology** 