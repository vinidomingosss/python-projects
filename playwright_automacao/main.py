from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador  = p.chromium.launch(headless=False) #headless =True - playwright cria o navegador sem aparecer na tela
    pagina = navegador.new_page()
    pagina.goto('https://docs.google.com/forms/d/e/1FAIpQLSecXqec_1aGgj9eUcW7T9GgECun3c_P4ZbgVc5CBZRDtiHHgA/viewform')
    pagina.fill('xpath=//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', 'vinicius')
    #pagina.locator('xpath=//*[@id="i9"]/div[3]/div').click() escolhe 1
    #pagina.locator('xpath=//*[@id="i12"]/div[3]/div').click() escolhe 2
    #pagina.locator('xpath=//*[@id="i15"]/div[3]/div').click() escolhe 3
    pagina.fill('xpath=//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[4]/div/span/div/div/div[1]/input', 'Testando a opção OUTRO') # escolhe outro
    pagina.locator('xpath=//*[@id="i26"]/div[2]').click()
    pagina.locator('xpath=//*[@id="i29"]/div[2]').click()
    pagina.locator('xpath=//*[@id="i32"]/div[2]').click()
    pagina.locator('text=Enviar').click()
    pagina.wait_for_selector('text=Sua resposta foi registrada.')
    pagina.locator('xpath=/html/body/div[1]/div[2]/div[1]/div').screenshot(path='Print usando locator.png')
    pagina.screenshot(path='Teste de print da tela.png', full_page=True) #Usa full_page quando tem barra de rolagem na pagina
    #time.sleep(3)

