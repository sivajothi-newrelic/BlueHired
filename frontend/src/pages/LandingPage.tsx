import React from 'react';
import {
  Box,
  Container,
  Typography,
  Button,
  Card,
  CardContent,
  CardActions,
  Chip,
  Paper,
} from '@mui/material';
import {
  Search as SearchIcon,
  Work as WorkIcon,
  People as PeopleIcon,
  TrendingUp as TrendingUpIcon,
  Construction,
  LocalShipping,
  Restaurant,
  Security,
} from '@mui/icons-material';
import { Link } from 'react-router-dom';

const LandingPage: React.FC = () => {
  const jobCategories = [
    { name: 'Construction', icon: <Construction />, count: '150+ Jobs' },
    { name: 'Transportation', icon: <LocalShipping />, count: '80+ Jobs' },
    { name: 'Hospitality', icon: <Restaurant />, count: '120+ Jobs' },
    { name: 'Security', icon: <Security />, count: '60+ Jobs' },
  ];

  const featuredJobs = [
    {
      title: 'Construction Worker',
      company: 'Construction Plus Pvt Ltd',
      location: 'Mumbai, Maharashtra',
      salary: '₹25,000 - ₹35,000',
      type: 'Full Time',
      skills: ['Carpentry', 'Safety Compliance'],
    },
    {
      title: 'Delivery Driver',
      company: 'Quick Delivery Services',
      location: 'Delhi, Delhi',
      salary: '₹20,000 - ₹30,000',
      type: 'Full Time',
      skills: ['Commercial Driving', 'Route Planning'],
    },
    {
      title: 'Security Guard',
      company: 'Security Pro Services',
      location: 'Pune, Maharashtra',
      salary: '₹16,000 - ₹20,000',
      type: 'Full Time',
      skills: ['Security Monitoring', 'Emergency Response'],
    },
  ];

  return (
    <Box>
      {/* Hero Section */}
      <Box
        sx={{
          background: 'linear-gradient(135deg, #1976d2 0%, #42a5f5 100%)',
          color: 'white',
          py: 8,
        }}
      >
        <Container maxWidth="lg">
          <Box
            sx={{
              display: 'flex',
              flexDirection: { xs: 'column', md: 'row' },
              alignItems: 'center',
              gap: 4,
            }}
          >
            <Box sx={{ flex: 1 }}>
              <Typography variant="h2" component="h1" gutterBottom fontWeight="bold">
                Find Your Next Blue-Collar Job
              </Typography>
              <Typography variant="h5" paragraph>
                Connect with top employers and discover opportunities in construction, 
                manufacturing, transportation, and more.
              </Typography>
              <Box sx={{ mt: 4, display: 'flex', gap: 2, flexWrap: 'wrap' }}>
                <Button
                  variant="contained"
                  size="large"
                  component={Link}
                  to="/jobs"
                  startIcon={<SearchIcon />}
                  sx={{
                    bgcolor: 'white',
                    color: 'primary.main',
                    '&:hover': { bgcolor: 'grey.100' },
                  }}
                >
                  Find Jobs
                </Button>
                <Button
                  variant="outlined"
                  size="large"
                  component={Link}
                  to="/register"
                  sx={{
                    borderColor: 'white',
                    color: 'white',
                    '&:hover': { borderColor: 'white', bgcolor: 'rgba(255,255,255,0.1)' },
                  }}
                >
                  Get Started
                </Button>
              </Box>
            </Box>
            <Box sx={{ flex: 1, display: 'flex', justifyContent: 'center' }}>
              <WorkIcon sx={{ fontSize: 200, opacity: 0.3 }} />
            </Box>
          </Box>
        </Container>
      </Box>

      {/* Stats Section */}
      <Container maxWidth="lg" sx={{ py: 6 }}>
        <Box
          sx={{
            display: 'flex',
            flexDirection: { xs: 'column', sm: 'row' },
            gap: 4,
            textAlign: 'center',
          }}
        >
          <Box sx={{ flex: 1 }}>
            <Paper elevation={2} sx={{ p: 3 }}>
              <WorkIcon color="primary" sx={{ fontSize: 48, mb: 2 }} />
              <Typography variant="h4" fontWeight="bold" color="primary">
                500+
              </Typography>
              <Typography variant="body1" color="text.secondary">
                Active Job Listings
              </Typography>
            </Paper>
          </Box>
          <Box sx={{ flex: 1 }}>
            <Paper elevation={2} sx={{ p: 3 }}>
              <PeopleIcon color="primary" sx={{ fontSize: 48, mb: 2 }} />
              <Typography variant="h4" fontWeight="bold" color="primary">
                1000+
              </Typography>
              <Typography variant="body1" color="text.secondary">
                Registered Job Seekers
              </Typography>
            </Paper>
          </Box>
          <Box sx={{ flex: 1 }}>
            <Paper elevation={2} sx={{ p: 3 }}>
              <TrendingUpIcon color="primary" sx={{ fontSize: 48, mb: 2 }} />
              <Typography variant="h4" fontWeight="bold" color="primary">
                95%
              </Typography>
              <Typography variant="body1" color="text.secondary">
                Success Rate
              </Typography>
            </Paper>
          </Box>
        </Box>
      </Container>

      {/* Job Categories */}
      <Box sx={{ bgcolor: 'grey.50', py: 6 }}>
        <Container maxWidth="lg">
          <Typography variant="h3" textAlign="center" gutterBottom fontWeight="bold">
            Popular Job Categories
          </Typography>
          <Typography variant="h6" textAlign="center" color="text.secondary" paragraph>
            Explore opportunities across various industries
          </Typography>
          <Box
            sx={{
              display: 'flex',
              flexWrap: 'wrap',
              gap: 3,
              mt: 4,
              justifyContent: 'center',
            }}
          >
            {jobCategories.map((category, index) => (
              <Box key={index} sx={{ minWidth: 250, flex: '1 1 250px', maxWidth: 300 }}>
                <Card
                  sx={{
                    textAlign: 'center',
                    p: 2,
                    cursor: 'pointer',
                    transition: 'transform 0.2s',
                    '&:hover': { transform: 'translateY(-4px)' },
                    height: '100%',
                  }}
                  component={Link}
                  to={`/jobs?category=${category.name}`}
                  style={{ textDecoration: 'none' }}
                >
                  <CardContent>
                    <Box sx={{ color: 'primary.main', mb: 2 }}>
                      {React.cloneElement(category.icon, { sx: { fontSize: 48 } })}
                    </Box>
                    <Typography variant="h6" gutterBottom>
                      {category.name}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      {category.count}
                    </Typography>
                  </CardContent>
                </Card>
              </Box>
            ))}
          </Box>
        </Container>
      </Box>

      {/* Featured Jobs */}
      <Container maxWidth="lg" sx={{ py: 6 }}>
        <Typography variant="h3" textAlign="center" gutterBottom fontWeight="bold">
          Featured Jobs
        </Typography>
        <Typography variant="h6" textAlign="center" color="text.secondary" paragraph>
          Latest opportunities from top employers
        </Typography>
        <Box
          sx={{
            display: 'flex',
            flexWrap: 'wrap',
            gap: 3,
            mt: 4,
            justifyContent: 'center',
          }}
        >
          {featuredJobs.map((job, index) => (
            <Box key={index} sx={{ minWidth: 300, flex: '1 1 300px', maxWidth: 400 }}>
              <Card sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
                <CardContent sx={{ flexGrow: 1 }}>
                  <Typography variant="h6" gutterBottom>
                    {job.title}
                  </Typography>
                  <Typography variant="body2" color="text.secondary" gutterBottom>
                    {job.company}
                  </Typography>
                  <Typography variant="body2" color="text.secondary" gutterBottom>
                    📍 {job.location}
                  </Typography>
                  <Typography variant="h6" color="primary" gutterBottom>
                    {job.salary}
                  </Typography>
                  <Chip label={job.type} size="small" sx={{ mb: 2 }} />
                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                    {job.skills.map((skill, skillIndex) => (
                      <Chip
                        key={skillIndex}
                        label={skill}
                        size="small"
                        variant="outlined"
                      />
                    ))}
                  </Box>
                </CardContent>
                <CardActions>
                  <Button
                    size="small"
                    component={Link}
                    to="/jobs"
                    sx={{ textTransform: 'none' }}
                  >
                    View Details
                  </Button>
                </CardActions>
              </Card>
            </Box>
          ))}
        </Box>
        <Box sx={{ textAlign: 'center', mt: 4 }}>
          <Button
            variant="contained"
            size="large"
            component={Link}
            to="/jobs"
            sx={{ textTransform: 'none' }}
          >
            View All Jobs
          </Button>
        </Box>
      </Container>

      {/* CTA Section */}
      <Box sx={{ bgcolor: 'primary.main', color: 'white', py: 6 }}>
        <Container maxWidth="lg" sx={{ textAlign: 'center' }}>
          <Typography variant="h3" gutterBottom fontWeight="bold">
            Ready to Get Started?
          </Typography>
          <Typography variant="h6" paragraph>
            Join thousands of job seekers and employers on BlueHired
          </Typography>
          <Box sx={{ mt: 4, display: 'flex', gap: 2, justifyContent: 'center', flexWrap: 'wrap' }}>
            <Button
              variant="contained"
              size="large"
              component={Link}
              to="/register"
              sx={{
                bgcolor: 'white',
                color: 'primary.main',
                '&:hover': { bgcolor: 'grey.100' },
              }}
            >
              Sign Up as Job Seeker
            </Button>
            <Button
              variant="outlined"
              size="large"
              component={Link}
              to="/register"
              sx={{
                borderColor: 'white',
                color: 'white',
                '&:hover': { borderColor: 'white', bgcolor: 'rgba(255,255,255,0.1)' },
              }}
            >
              Post Jobs as Employer
            </Button>
          </Box>
        </Container>
      </Box>
    </Box>
  );
};

export default LandingPage;
