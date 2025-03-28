from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar o WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Acessar a página da Receita Federal
driver.get("https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp")

# Aguardar a página carregar
time.sleep(5)

# Procurar o elemento que contém a sitekey
try:
    captcha_div = driver.find_element(By.XPATH, "//div[contains(@class, 'h-captcha')]")
    sitekey = captcha_div.get_attribute("data-sitekey")
    print(f"🔑 Sitekey encontrada: {sitekey}")
except Exception as e:
    print("❌ Não foi possível encontrar a sitekey.", e)

# Fechar o navegador
driver.quit()
