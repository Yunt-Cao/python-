import turtle
import time

def draw_heart():
    # 设置画笔
    t = turtle.Turtle()
    t.speed(3)
    t.pensize(2)
    
    # 设置窗口背景色
    window = turtle.Screen()
    window.bgcolor("black")
    
    # 绘制红色爱心
    t.color("red")
    t.begin_fill()
    
    # 爱心的绘制路径
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    
    t.end_fill()
    
    # 移动到爱心下方写文字
    t.up()
    t.goto(0, -150)
    t.down()
    t.color("white")
    t.write("Love You", align="center", font=("Arial", 15, "bold"))
    
    # 隐藏画笔
    t.hideturtle()
    
    # 暂停3秒后关闭窗口
    time.sleep(3)
    window.bye()

if __name__ == "__main__":
    draw_heart()