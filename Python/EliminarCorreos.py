import pyautogui
import time

# Define las coordenadas del punto donde quieres hacer clic
x_clic, y_clic = 950, 300

# Bucle para realizar 3000 clics
for i in range(1):
    for _ in range(100):
        # Mueve el mouse a las coordenadas especificadas
        pyautogui.moveTo(x_clic, y_clic)

        # Realiza un clic
        pyautogui.click()

        # Espera un breve momento antes del siguiente clic (ajusta según sea necesario)
        #time.sleep(0.1)
