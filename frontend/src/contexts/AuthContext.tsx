import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { User, JobSeekerProfile, JobPosterProfile, AuthContextType, RegisterData } from '../types';
import { authAPI } from '../services/api';

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [profile, setProfile] = useState<JobSeekerProfile | JobPosterProfile | null>(null);
  const [loading, setLoading] = useState(true);

  const isAuthenticated = !!user;

  useEffect(() => {
    const initAuth = async () => {
      const token = localStorage.getItem('authToken');
      if (token) {
        try {
          const userData = await authAPI.getCurrentUser();
          setUser(userData);
          // TODO: Fetch user profile based on role
        } catch (error) {
          console.error('Failed to get current user:', error);
          localStorage.removeItem('authToken');
        }
      }
      setLoading(false);
    };

    initAuth();
  }, []);

  const login = async (email: string, password: string) => {
    try {
      const response = await authAPI.login({ email, password });
      const { token, user: userData } = response;
      
      localStorage.setItem('authToken', token);
      setUser(userData);
      
      // TODO: Fetch user profile based on role
    } catch (error) {
      console.error('Login failed:', error);
      throw error;
    }
  };

  const register = async (userData: RegisterData) => {
    try {
      const response = await authAPI.register(userData);
      const { token, user: newUser } = response;
      
      localStorage.setItem('authToken', token);
      setUser(newUser);
      
      // TODO: Create user profile based on role
    } catch (error) {
      console.error('Registration failed:', error);
      throw error;
    }
  };

  const logout = () => {
    localStorage.removeItem('authToken');
    setUser(null);
    setProfile(null);
    // Optional: Call logout API endpoint
    authAPI.logout().catch(console.error);
  };

  const value: AuthContextType = {
    user,
    profile,
    login,
    register,
    logout,
    loading,
    isAuthenticated,
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};
