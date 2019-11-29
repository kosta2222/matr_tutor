import numpy as np
np.random.seed(0)
# Берем квадратное изображение 3x3 заполняем
# числами от 0 до 20,вытягиваем его в ленту
X = np.random.randint(0, 20, (3, 3)).flatten().tolist()
# Берем ядро 2x2
W0 = np.random.randint(0, 10, (2,2)).tolist()
def conv(inputt, kernel, width, height, stride):
    """
    Кросс-кореляция(как бы свертка)
    :param input: изображение как лента
    :param kernel: 2d ядро
    :param width: ширина изначального изображения
    :param height: его высота
    :param stride: шаг при свертке
    :return:выходную карту признаков
    """
    kernel_width = len(kernel[0])
    kernel_height = kernel_width
    v = (((width - kernel_width) // stride) + 1)  # выходной обьем(ширина) выходной карты признаков
    # выходная карта признаков квадратная
    output = [0] * (v ** 2)
    n = 0
    for j in range(height - stride):
        for i in range(width - stride):
            result = 0
            element_exists = False
            for a in range(kernel_height):
                for b in range(kernel_width):
                    Y = j * stride + a
                    X = i * stride + b
                    if Y >= height or X >= width:
                        continue
                    result += inputt[Y * width + X] * kernel[a][b]
                    element_exists = True
            if element_exists:
                if n == len(output):
                    break
                output[n] = result
                n += 1
    return output
# производим свертку
print(conv(X,W0,3,3,1))
#-->[195, 134, 239, 319]
print(conv(X,W0,3,3,2))
#-->[195]

