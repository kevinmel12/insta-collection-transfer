from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager

import requests
from bs4 import BeautifulSoup

import time

# Configurer les options du navigateur
options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])


 # ------------------------------- PREMIER COMPTE INSTA -------------------------------


# Créer une instance de WebDriver
browser1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Ouvrir la page web Instagram
    url = "https://www.instagram.com/"
    browser1.get(url)


    # Attendre et interagir enlever la pop-up des cookies après l'ouverture de la page
    time.sleep(2)
    WebDriverWait(browser1, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
    )).click()

    time.sleep(5)


    # Lire le mot de passe et le pseudo à partir du fichier `.env`
    with open('.env', 'r') as file:
        lines = file.readlines()
        username = lines[0].strip().split('=')[1]
        password = lines[1].strip().split('=')[1]

    # Remplir les champs d'authentification
    WebDriverWait(browser1, 10).until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(username)
    browser1.find_element(By.NAME, 'password').send_keys(password)

    # Cliquer sur le bouton de connexion
    WebDriverWait(browser1, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[3]/button')
    )).click()

    time.sleep(10)  

    # Naviguer vers la page de collection
    saves_url = f"https://www.instagram.com/{username}/saved/_/17901925336598446/"
    browser1.get(saves_url) 


    # Attendre que la page se charge
    WebDriverWait(browser1, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))


    time.sleep(10) 


    # ------------------------------- EXTRACTION DES LIENS DES PUBLICATIONS -------------------------------


    # Défilement de la page pour charger le contenu
    SCROLL_PAUSE_TIME = 2
    last_height = browser1.execute_script("return document.body.scrollHeight")

    while True:
        browser1.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)

        # Calcule de la nouvelle hauteur de scroll et comparaison avec la dernière hauteur de scroll
        new_height = browser1.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    

    # Extraction des liens des publications
    links = WebDriverWait(browser1, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/p/')]"))
    )

    # Impression des liens
    for link in links:
        print(link.get_attribute('href'))

    # Stock des liens dans un fichier
    with open('instagram_links.txt', 'w') as f:
        for link in links:
            f.write(link.get_attribute('href') + '\n')

    print(f"Nbr total de liens extraits : {len(links)}")
    

    # ------------------------------- FERMETURE DE LA FENETRE POUR LE PREMIER COMPTE -------------------------------

    # time.sleep du premier compte
    time.sleep(5)
finally:
    browser1.quit()

    # ------------------------------- SECOND COMPTE INSTA -------------------------------


def open_link_in_new_window(driver, link):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(link)

#Pour trouver le bouton d'enregistrement pour la collection
def find_and_click_save_button(driver):
    selectors = [
        (By.XPATH, '//div[@role="button" and @aria-label="Enregistrer"]'),
        (By.XPATH, '//button[@aria-label="Enregistrer"]'),
        (By.XPATH, '//div[contains(@aria-label, "Enregistrer")]'),
        (By.XPATH, '//span[text()="Enregistrer"]/ancestor::button'),
        (By.CSS_SELECTOR, '[aria-label="Enregistrer"]'),
        (By.XPATH, '//svg[@aria-label="Enregistrer"]/parent::button'),
    ]

    #Exécution du code juste au-dessus
    for selector in selectors:
        try:
            element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(selector))
            # Quand le bouton est trouvé, cliquer dessus
            element.click()
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@role="button" and @aria-label="Enregistré"]')))
            return True
        except (TimeoutException, ElementClickInterceptedException):
            continue
    return False

options = Options()
options.add_argument("--start-maximized")

browser2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
try:
    # Ouvrir la page web Instagram dans la nouvelle fenêtre
    url = "https://www.instagram.com/"
    browser2.get(url)


    # Attendre et interagir enlever la pop-up des cookies après l'ouverture de la page
    time.sleep(2)
    WebDriverWait(browser2, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
    )).click()

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

    # Attente de connxion
    time.sleep(10) 


    # Naviguer vers la page de collection
    saves_url = f"https://www.instagram.com/{username}/saved/_/17927259749817910/"
    browser2.get(saves_url)

    #Attente de la connexion à la page
    time.sleep(10) 
    WebDriverWait(browser2, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))


 # Lire et ouvrir les liens à partir du fichier
    with open('instagram_links.txt', 'r') as file:
        links = file.read().splitlines()
        for link in links:
            open_link_in_new_window(browser2, link.strip())
            time.sleep(5)  # Attendre 5 secondes entre chaque ouverture de lien

            # Essayer de trouver et cliquer sur le bouton "Enregistrer"
            if find_and_click_save_button(browser2):
                print(f"Publication enregistrée avec succès : {link}")
            else:
                print(f"Impossible d'enregistrer la publication : {link}")
            
            time.sleep(3)  # Attendre 3 secondes avant de passer au lien suivant

    # Attendre avant de fermer le navigateur
    time.sleep(9000)
    
        
# time.sleep du second compte
    time.sleep(9000)

finally:
    browser2.quit()
    

