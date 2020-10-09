from django.test import TestCase
#from django.contrib.auth import get_peak_model
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
			email=email,
			password=password
		)
    def test_new_user_email_normalized(self):
	    """Test the email for a new user is normalized"""
	    email = 'test@test.com'
	    user = get_user_model().objects.create_user(email, 'test123')
	
	    self.assertEqual(user.email, email.lower())
    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


#    def test_creat_peak_successful(self):
#        """Test creating a new pick successful"""
#        lat = 3.1
#        lon = 10.0
#        altitude = 2.3 
#        name = 'peak_name'
#        peak = get_peak_model().objects.create_peak(
#            lat = lat,
#            lon = lon,
#            altitude = altitude, 
#            name = name   
#        )
#        self.assertEqual(peak.lat,lat)
#        self.assertEqual(peak.lon,lon)
#        self.assetEqual(peak.altitude,altitude)
#        self.assertEqual(peak.name,name)
