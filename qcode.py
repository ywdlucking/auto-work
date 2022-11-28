import qrcode

qr = qrcode.QRCode(
    version=2,  # 尺寸
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 容错信息当前为 7% 容错
    box_size=10,  # 每个格子的像素大小
    border=1  # 边框格子宽度
)  # 设置二维码的大小

qr.add_data("https://www.csdn.net/")  # 指定 url
img = qr.make_image()  # 生成二维码图片
img.save("output/csdn.png")  # 保存
