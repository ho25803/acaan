import flet as ft
import random

def main(page: ft.Page):
    page.title = "ACAAN Trainer"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 데이터
    suits = ['♠', '♦', '♣', '♥']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    # UI 요소
    result_text = ft.Text("READY", size=50, weight=ft.FontWeight.BOLD)
    
    def generate(e):
        rank = random.choice(ranks)
        suit = random.choice(suits)
        number = random.randint(1, 52)
        result_text.value = f"{number}\n{rank}{suit}"
        page.update()

    # 앱 화면 구성 (ft.colors를 ft.Colors로 변경)
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("ACAAN TRAINING", size=20, color=ft.Colors.GREY),
                result_text,
                ft.ElevatedButton("출력", on_click=generate, height=60, width=200)
            ], alignment=ft.MainAxisAlignment.CENTER),
            padding=20
        )
    )

# 최신 권장 방식인 run() 사용
ft.run(main, port=8550)