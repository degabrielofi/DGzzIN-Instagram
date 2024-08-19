from PIL import Image
import pyautogui
import logging
import os
import win32gui

class ScreenManager: 

    @staticmethod
    def is_app_focused(app_title_name: str):
        active_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower()     
        return app_title_name.lower() in active_window_title
    
    @staticmethod
    def click_on_screen(coordinate_to_click: tuple):
        if coordinate_to_click:
            pyautogui.click(coordinate_to_click)
        else:
            logging.info("Coordenada inválida para clicar na tela.")

    @staticmethod
    def scroll_on_screen(value_to_scroll: int):
        pyautogui.scroll(value_to_scroll)
    
    @staticmethod
    def search_image_on_screen(image_to_search: str):
        # Transforma o caminho relativo em caminho absoluto
        absolute_image_path = os.path.abspath(image_to_search)
        
        # Verifica se o arquivo existe
        if not os.path.isfile(absolute_image_path):
            logging.error(f"A imagem '{absolute_image_path}' não foi encontrada no diretório especificado.")
            return None

        try:
            # Abre a imagem para verificar se ela pode ser carregada
            Image.open(absolute_image_path)
            
            # Procura todas as ocorrências da imagem na tela
            found_locations = list(pyautogui.locateAllOnScreen(image=absolute_image_path, grayscale=True, confidence=0.9))
            
            if found_locations:
                return found_locations
            else:
                logging.info(f"A imagem '{absolute_image_path}' não foi encontrada na tela.")
                return None
                
        except Exception as ex:
            logging.error(f"Erro ao procurar a imagem na tela! \nError: {ex}", exc_info=True)
            return None
