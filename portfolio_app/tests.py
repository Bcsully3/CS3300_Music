from django.test import *
from django.urls import reverse
from .models import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
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
    def test_add_update_delete_piece(self):
        self.browser.get("http://127.0.0.1:8000/")

        musicians_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'id_musicians')))
        musicians_link.click()

        musician_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'test name')))
        musician_link.click()

        add_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'add_piece')))
        add_link.click()

        title_box = self.browser.find_element(By.ID,'title_id')
        genre_box = self.browser.find_element(By.ID, 'genre_id')
        mp3_box = self.browser.find_element(By.ID, "mp3_file_id")

        # Interact with the "piece_type" dropdown using its id attribute
        piece_type_dropdown = Select(self.browser.find_element(By.ID, "piece_type_id"))

        # Select a value from the dropdown (replace "Your Piece Type" with the actual value)
        piece_type_dropdown.select_by_visible_text("Other")
        title_box.send_keys("Test Title")
        genre_box.send_keys("Test Genre")
        mp3_box.send_keys("C:/Users/brend/Downloads/Oli Parker - Havana (Unofficial Music Video).mp3")
        
        submit_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'submit')))
        submit_link.click()

        #back on musician detail view, click on piece view
        view_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'view')))
        view_link.click()

        ###   UPDATE

        #click on piece update
        update_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'update')))
        update_link.click()

        #change genre

        genre_box = self.browser.find_element(By.ID, 'genre_id')
        genre_box.send_keys("Test Genre 2")

        #submit update
        submit_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'submit_update')))
        submit_link.click()

        ##### DELETE
        
        #click on delete piece and confirm
        delete_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'delete')))
        delete_link.click()

        confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'confirm')))
        confirm_button.click()

        #make sure it returns to home page
        home = self.browser.find_element(By.ID, 'home')
        self.assertIsNotNone(home)


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


