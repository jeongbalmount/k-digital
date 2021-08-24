from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
# import RPi_I2C_driver
# import RPi.GPIO as GPIO
import time

# from GPIO에 해당하는 라이브러리 호출

# buzzer = 26
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(buzzer, GPIO.OUT)
# GPIO.setwarnings(False)


def index(request):
    return HttpResponse("Hello world")


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = request.POST
        dict = post.dict()
        # lcd = RPi_I2C_driver.lcd(0x27)
        # lcd.print(dict['inputText'])

        # pwm = GPIO.PWM(buzzer, 262)
        # pwm.start(50.0)
        # time.sleep(1.0)

        # pwm.stop()

        print(dict['inputText'])
        # text = form.inputText
        # print(text)
    else:
        form = PostForm()

    return render(request, 'pi/insertText.html', {'form': form, })

