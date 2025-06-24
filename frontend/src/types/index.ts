export interface User {
  id: string;
  email: string;
  first_name: string;
  last_name: string;
  role: 'job_seeker' | 'job_poster' | 'admin';
  phone_number?: string;
  is_verified: boolean;
  created_at: string;
}

export interface JobSeekerProfile {
  id: string;
  user: User;
  bio?: string;
  experience_level: 'entry' | 'mid' | 'senior' | 'expert';
  location?: string;
  city?: string;
  state?: string;
  pincode?: string;
  availability: boolean;
  expected_salary_min?: number;
  expected_salary_max?: number;
  skills: JobSeekerSkill[];
}

export interface JobPosterProfile {
  id: string;
  user: User;
  company_name: string;
  company_description?: string;
  company_size?: string;
  industry?: string;
  website?: string;
  address?: string;
  city?: string;
  state?: string;
  pincode?: string;
  contact_phone?: string;
  is_company_verified: boolean;
}

export interface Skill {
  id: string;
  name: string;
  category: string;
  description?: string;
}

export interface JobSeekerSkill {
  id: string;
  skill: Skill;
  proficiency_level: 'beginner' | 'intermediate' | 'advanced' | 'expert';
  years_of_experience: number;
}

export interface JobCategory {
  id: string;
  name: string;
  description?: string;
  icon?: string;
  is_active: boolean;
}

export interface Job {
  id: string;
  title: string;
  description: string;
  category: JobCategory;
  posted_by: User;
  company: JobPosterProfile;
  job_type: 'full_time' | 'part_time' | 'contract' | 'temporary' | 'internship';
  experience_level: 'entry' | 'mid' | 'senior' | 'expert';
  location: string;
  city: string;
  state: string;
  pincode?: string;
  is_remote: boolean;
  salary_min?: number;
  salary_max?: number;
  salary_type: 'hourly' | 'daily' | 'weekly' | 'monthly' | 'yearly' | 'project';
  salary_negotiable: boolean;
  requirements?: string;
  benefits?: string;
  application_deadline?: string;
  max_applications?: number;
  status: 'draft' | 'active' | 'paused' | 'closed' | 'expired';
  is_featured: boolean;
  views_count: number;
  applications_count: number;
  created_at: string;
  updated_at: string;
  published_at?: string;
  skill_requirements: JobSkillRequirement[];
}

export interface JobSkillRequirement {
  id: string;
  skill: Skill;
  requirement_level: 'required' | 'preferred' | 'nice_to_have';
  min_experience_years: number;
}

export interface JobApplication {
  id: string;
  job: Job;
  applicant: User;
  job_seeker_profile: JobSeekerProfile;
  cover_letter?: string;
  status: 'pending' | 'under_review' | 'shortlisted' | 'rejected' | 'hired';
  applied_at: string;
  reviewed_at?: string;
  notes?: string;
}

export interface AuthContextType {
  user: User | null;
  profile: JobSeekerProfile | JobPosterProfile | null;
  login: (email: string, password: string) => Promise<void>;
  register: (userData: RegisterData) => Promise<void>;
  logout: () => void;
  loading: boolean;
  isAuthenticated: boolean;
}

export interface RegisterData {
  email: string;
  password: string;
  first_name: string;
  last_name: string;
  role: 'job_seeker' | 'job_poster';
  phone_number?: string;
  company_name?: string; // For job posters
}

export interface LoginData {
  email: string;
  password: string;
}

export interface JobFilters {
  search?: string;
  category?: string;
  location?: string;
  job_type?: string;
  experience_level?: string;
  salary_min?: number;
  salary_max?: number;
  is_remote?: boolean;
}

export interface PaginatedResponse<T> {
  count: number;
  next?: string;
  previous?: string;
  results: T[];
}
