import pygame
pygame.init()
window=pygame.display.set_mode((1200,400))
track=pygame.image.load('track6.png')
car=pygame.image.load('tesla.png')
# car size
car=pygame.transform.scale(car,(30,60))
car_x=155
car_y=300
focal_dis=25
camera_x_offset= 0
camera_y_offset =0
direction= 'up'
drive=True
clock=pygame.time.Clock()
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive =False
            
    clock.tick(60)
    camera_x=car_x + camera_x_offset + 15
    camera_y=car_y + camera_y_offset+ 15
    up_px= window.get_at((camera_x, camera_y - focal_dis))[0]
    down_px= window.get_at((camera_x, camera_y + focal_dis))[0]
    right_px=window.get_at((camera_x  + focal_dis,camera_y))[0]
    print(up_px,right_px,down_px)
    
    # change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px ==255:
        direction = 'right'
        camera_x_offset=30
        car = pygame.transform.rotate(car,-90)
    elif direction == 'right' and right_px !=255 and down_px ==255:
        direction = 'down'
        car_x= car_x+30
        camera_x_offset= 0
        camera_y_offset =30
        car = pygame.transform.rotate(car,-90)
    elif direction == 'down' and down_px !=255 and right_px ==255:
        direction='right'
        car_y =car_y +30
        camera_x_offset=30
        camera_y_offset=0
        car=pygame.transform.rotate(car,90)
    elif direction =='right' and right_px !=255 and up_px ==255:
        direction='up'
        car_x=car_x+30
        camera_x_offset=0
        car=pygame.transform.rotate(car,90)
        
    # drive
    if direction == 'up' and up_px == 255:
        car_y=car_y-2
    elif direction=='right' and right_px==255:
        car_x =car_x + 2
    elif direction == 'down' and down_px == 255:
        car_y= car_y +2
    window.blit(track, (0,0))
    window.blit(car,(car_x,car_y))
    pygame.draw.circle(window,(0,255,0),(camera_x,camera_y),5,5)
    pygame.display.update()
    