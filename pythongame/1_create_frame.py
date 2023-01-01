import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("죠죠의 기묘한 모험")

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하는 상태인 건지 체크
        if event.type == pygame.QUIT: #x창을 눌러 게임을 껐을 때 발생하는 이벤트
            running = False #게임이 진행중이 아닐때

#pygame 종료
pygame.quit()