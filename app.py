from screen_manager import ScreenManager
import time
import random
import keyboard

def run():
    total_follows_count = 0

    while True:
        if ScreenManager.is_app_focused(app_title_name="instagram"):
            coordinates = ScreenManager.search_image_on_screen(image_to_search="./assets/follow_button.png")
            
            if coordinates: 
                for coordinate in coordinates:
                    total_follows_count += 1  
                    ScreenManager.click_on_screen(coordinate_to_click=coordinate)
                    time.sleep(random.randint(1, 2))
            else:
                print("Botão de seguir não encontrado.")

        ScreenManager.scroll_on_screen(value_to_scroll=-400)
        time.sleep(random.randint(1, 2))
        print(f"Total de follows feitos até o momento: {total_follows_count}")

        if keyboard.is_pressed("ESC"):
            print("DGzzIN Instagram Fechando...")
            break

run()
