from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurer les options du navigateur
options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])


 # ------------------------------- PREMIER COMPTE INSTA -------------------------------


# Créer une instance de WebDriver
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Ouvrir la page web Instagram
    url = "https://www.instagram.com/"
    browser.get(url)


    # Attendre et interagir avec l'élément après l'ouverture de la page
    time.sleep(2)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
    )).click()

    time.sleep(5)


    # Lire le mot de passe et le pseudo à partir du fichier `.env`
    with open('.env', 'r') as file:
        lines = file.readlines()
        username = lines[0].strip().split('=')[1]
        password = lines[1].strip().split('=')[1]

    # Remplir les champs d'authentification
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(username)
    browser.find_element(By.NAME, 'password').send_keys(password)

    # Cliquer sur le bouton de connexion
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[3]/button')
    )).click()

    time.sleep(10)  

    # Naviguer vers la page de collection
    saves_url = f"https://www.instagram.com/{username}/saved/_/17901925336598446/"
    browser.get(saves_url)

    # Attendre que la page se charge
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))


    # ------------------------------- SECOND COMPTE INSTA -------------------------------


    browser2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        # Ouvrir la page web Instagram dans la nouvelle fenêtre
        url = "https://www.instagram.com/"
        browser2.get(url)


        # Attendre et interagir avec l'élément après l'ouverture de la page
        time.sleep(2)
        WebDriverWait(browser2, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        )).click()

        time.sleep(5)

            # Lire le mot de passe et le pseudo à partir du fichier `.env`
        with open('.env', 'r') as file:
            lines = file.readlines()
            username = lines[2].strip().split('=')[1]
            password = lines[3].strip().split('=')[1]

        # Remplir les champs d'authentification
        WebDriverWait(browser2, 10).until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(username)
        browser2.find_element(By.NAME, 'password').send_keys(password)

        # Cliquer sur le bouton de connexion
        WebDriverWait(browser2, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[3]/button')
        )).click()

        time.sleep(10)  

        # Naviguer vers la page de collection
        saves_url = f"https://www.instagram.com/{username}/saved/_/17927259749817910/"
        browser2.get(saves_url)


        # Attendre que la page se charge
        WebDriverWait(browser2, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            

        time.sleep(9000)
    finally:
        browser2.quit()


    time.sleep(9000)
finally:
    browser.quit()

 