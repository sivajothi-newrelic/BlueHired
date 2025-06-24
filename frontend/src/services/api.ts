import axios from 'axios';
import { User, Job, JobApplication, JobCategory, Skill, PaginatedResponse, JobFilters, RegisterData, LoginData } from '../types';

const API_BASE_URL = 'http://localhost:8001';

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('authToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth API
export const authAPI = {
  login: async (data: LoginData) => {
    const response = await api.post('/auth/login/', data);
    return response.data;
  },

  register: async (data: RegisterData) => {
    const response = await api.post('/auth/register/', data);
    return response.data;
  },

  logout: async () => {
    const response = await api.post('/auth/logout/');
    return response.data;
  },

  getCurrentUser: async (): Promise<User> => {
    const response = await api.get('/auth/user/');
    return response.data;
  },

  refreshToken: async () => {
    const response = await api.post('/auth/refresh/');
    return response.data;
  },
};

// Jobs API
export const jobsAPI = {
  getJobs: async (filters?: JobFilters): Promise<PaginatedResponse<Job>> => {
    const params = new URLSearchParams();
    if (filters) {
      Object.entries(filters).forEach(([key, value]) => {
        if (value !== undefined && value !== null && value !== '') {
          params.append(key, value.toString());
        }
      });
    }
    const response = await api.get(`/jobs/?${params.toString()}`);
    return response.data;
  },

  getJob: async (id: string): Promise<Job> => {
    const response = await api.get(`/jobs/${id}/`);
    return response.data;
  },

  createJob: async (jobData: Partial<Job>) => {
    const response = await api.post('/jobs/', jobData);
    return response.data;
  },

  updateJob: async (id: string, jobData: Partial<Job>) => {
    const response = await api.put(`/jobs/${id}/`, jobData);
    return response.data;
  },

  deleteJob: async (id: string) => {
    const response = await api.delete(`/jobs/${id}/`);
    return response.data;
  },

  applyToJob: async (jobId: string, applicationData: { cover_letter?: string }) => {
    const response = await api.post(`/jobs/${jobId}/apply/`, applicationData);
    return response.data;
  },
};

// Categories API
export const categoriesAPI = {
  getCategories: async (): Promise<JobCategory[]> => {
    const response = await api.get('/categories/');
    return response.data;
  },
};

// Skills API
export const skillsAPI = {
  getSkills: async (): Promise<Skill[]> => {
    const response = await api.get('/skills/');
    return response.data;
  },
};

// Applications API
export const applicationsAPI = {
  getMyApplications: async (): Promise<JobApplication[]> => {
    const response = await api.get('/applications/my/');
    return response.data;
  },

  getJobApplications: async (jobId: string): Promise<JobApplication[]> => {
    const response = await api.get(`/jobs/${jobId}/applications/`);
    return response.data;
  },

  updateApplicationStatus: async (applicationId: string, status: string) => {
    const response = await api.patch(`/applications/${applicationId}/`, { status });
    return response.data;
  },
};

export default api;
