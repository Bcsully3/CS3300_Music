from django.test import *
from django.urls import reverse
from .models import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Edge()

# webdriver test for login with test user
class LoginTest(LiveServerTestCase):
    def setUp(self):
        self.browser=driver
    def test_login(self):
        self.browser.get("http://127.0.0.1:8000/")

        login_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login')))
        login_link.click()

        # The user sees a form to enter the username and password
        username_input = self.browser.find_element(By.ID,'id_username')
        password_input = self.browser.find_element(By.ID,'id_password')

        # The user types in username and password
        username_input.send_keys('test')
        password_input.send_keys('testpassword')

        # The user submits the form
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login_button')))
        login_button.click()

        # The user sees the new post on the list page
        logout_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'logout')))
        self.assertIsNotNone(logout_link)


# webdriver test for viewing a musician
class ViewMusician(LiveServerTestCase):
    def setUp(self):
        self.browser=driver
    def tearDown(self):
        self.browser.quit()
    def test_musician_view(self):
        self.browser.get("http://127.0.0.1:8000/")

        musicians_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'id_musicians')))
        musicians_link.click()

        musician_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'test name')))
        musician_link.click()

        update_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'update')))
        add_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'add_piece')))

        self.assertIsNotNone(update_link)
        self.assertIsNotNone(add_link)



class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

class MusicianModelTest(TestCase):
    def setUp(self):
        self.musician = Musician.objects.create(
            name="Test Musician",
            email="test@gmail.com",
            main_instrument="AG"
        )
    
    def test_musician_creation(self):
        self.assertEqual(self.musician.name, "Test Musician")
        self.assertEqual(self.musician.email, "test@gmail.com")
        self.assertEqual(self.musician.main_instrument, "AG")

class PieceModelTest(TestCase):
    def setUp(self):
        self.musician = Musician.objects.create(
            name="Test Musician",
            email="test@gmail.com",
            main_instrument="AG"
        )
        self.piece = Piece.objects.create(
            title="Test Piece",
            genre="Test Genre",
            piece_type="CR",
            musician=self.musician
        )

    def test_piece_creation(self):
        self.assertEqual(self.piece.title, "Test Piece")
        self.assertEqual(self.piece.genre, "Test Genre")
        self.assertEqual(self.piece.piece_type, "CR")
        self.assertEqual(self.piece.musician, self.musician)


