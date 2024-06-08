# api/scraper.py
from typing import Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class CoinMarketCapScraper:
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    def scrape_coin(self,coin):
        url = f"https://coinmarketcap.com/currencies/{coin}/"
        self.driver.get(url)

        if coin!='DUKO':
            data={
                "..":self._get_text(By.CSS_SELECTOR, '#__next > div > div.container.cmc-main-section > div > div.sc-404__StyledError-ic5ef7-0.fygxIm > p.Text-sc-1eb5slv-0.ebuPNT')
            }
        else:
            data = {
                
                "price": self._get_text(By.CSS_SELECTOR, '#section-coin-overview > div.sc-d1ede7e3-0.gNSoet.flexStart.alignBaseline > span'),
                "price_change": self._get_text(By.CSS_SELECTOR, '#section-coin-overview > div.sc-d1ede7e3-0.gNSoet.flexStart.alignBaseline > div > div > p'),
                "market_cap": self._get_text(By.CSS_SELECTOR, '#section-coin-stats > div > dl > div:nth-child(1) > div.sc-d1ede7e3-0.sc-cd4f73ae-0.bwRagp.iWXelA.flexBetween > dd'),
                "market_cap_rank": self._get_text(By.CSS_SELECTOR, '#section-coin-stats > div > dl > div:nth-child(1) > div.sc-d1ede7e3-0.sc-cd4f73ae-3.bwRagp.iElHRj.BasePopover_base__tgkdS > div > span'),
                "volume": self._get_text(By.CSS_SELECTOR, '#section-coin-stats > div > dl > div:nth-child(2) > div.sc-d1ede7e3-0.sc-cd4f73ae-0.bwRagp.iWXelA.flexBetween > dd'),
                "volume_rank": self._get_text(By.CSS_SELECTOR, '#section-coin-stats > div > dl > div:nth-child(2) > div.sc-d1ede7e3-0.sc-cd4f73ae-3.bwRagp.iElHRj.BasePopover_base__tgkdS > div > span'),
                "volume_change": self._get_text(By.CSS_SELECTOR, '#section-coin-stats > div > dl > div:nth-child(3) > div > dd'),
                "circulating_supply": self._get_text(By.CSS_SELECTOR, '#section-coin-stats > div > dl > div:nth-child(4) > div > dd'),
                "total_supply": self._get_text(By.CSS_SELECTOR, '#section-coin-stats > div > dl > div:nth-child(5) > div > dd'),
                "diluted_market_cap": self._get_text(By.CSS_SELECTOR, '#section-coin-stats > div > dl > div:nth-child(7) > div > dd'),
                "contracts": self._get_contracts(),
                "official_links": self._get_official_links(),
                "socials": self._get_socials()
                
            }
        return data

    def _get_text(self, by, value):
        try:
            return self.driver.find_element(by, value).text
        except Exception as e:
            return str(e)
        
        

    def _get_contracts(self):
        contracts = []
        contract_elements = self.driver.find_elements(By.CSS_SELECTOR, '#__next > div.sc-8fab8d8d-1.kYUKSZ.global-layout-v2 > div > div.cmc-body-wrapper > div > div > div.sc-4c05d6ef-0.sc-55349342-0.dlQYLv.gELPTu.coin-stats > div.sc-d1ede7e3-0.jLnhLV > section:nth-child(2) > div > div.sc-d1ede7e3-0.cvkYMS.coin-info-links > div:nth-child(1) > div.sc-d1ede7e3-0.bwRagp > div > div > a')
        for element in contract_elements:
            link = element.get_attribute('href')
            name = element.text.strip()
            contracts.append({"name": name, "url": link})
        return contracts

    def _get_official_links(self):
        links = []
        link_elements = self.driver.find_elements(By.CSS_SELECTOR, '#__next > div.sc-8fab8d8d-1.kYUKSZ.global-layout-v2 > div > div.cmc-body-wrapper > div > div > div.sc-4c05d6ef-0.sc-55349342-0.dlQYLv.gELPTu.coin-stats > div.sc-d1ede7e3-0.jLnhLV > section:nth-child(2) > div > div.sc-d1ede7e3-0.cvkYMS.coin-info-links > div:nth-child(2) > div.sc-d1ede7e3-0.bwRagp > div > div > a')
        for element in link_elements:
            link = element.get_attribute('href')
            name = element.text.strip()
            links.append({"name": name, "url": link})
        return links

    def _get_socials(self):
        socials = []
        social_element_1 = self.driver.find_elements(By.CSS_SELECTOR, '#__next > div.sc-8fab8d8d-1.kYUKSZ.global-layout-v2 > div > div.cmc-body-wrapper > div > div > div.sc-4c05d6ef-0.sc-55349342-0.dlQYLv.gELPTu.coin-stats > div.sc-d1ede7e3-0.jLnhLV > section:nth-child(2) > div > div.sc-d1ede7e3-0.cvkYMS.coin-info-links > div:nth-child(3) > div.sc-d1ede7e3-0.bwRagp > div > div:nth-child(1) > a')
        for element in social_element_1:
            link = element.get_attribute('href')
            name = element.text.strip()
            socials.append({"name": name, "url": link})
        social_element_2 = self.driver.find_elements(By.CSS_SELECTOR, '#__next > div.sc-8fab8d8d-1.kYUKSZ.global-layout-v2 > div > div.cmc-body-wrapper > div > div > div.sc-4c05d6ef-0.sc-55349342-0.dlQYLv.gELPTu.coin-stats > div.sc-d1ede7e3-0.jLnhLV > section:nth-child(2) > div > div.sc-d1ede7e3-0.cvkYMS.coin-info-links > div:nth-child(3) > div.sc-d1ede7e3-0.bwRagp > div > div:nth-child(2) > a')
        for element in social_element_2:
            link = element.get_attribute('href')
            name = element.text.strip()
            socials.append({"name": name, "url": link})    
        return socials


    def close(self):
        self.driver.quit()