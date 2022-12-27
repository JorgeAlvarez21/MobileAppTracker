import flet as ft

def main(page: ft.Page):


    a = ft.Container(
        width=400,
        height=400,
        bgcolor=ft.colors.BLUE,
    )

    b = ft.Container(
        width=200,
        height=200,
        bgcolor=ft.colors.WHITE,
    )


    c = ft.Container(
        width=150,
        height=150,
        bgcolor="blue",
        border_radius=10,
        offset=ft.transform.Offset(-2, 0),
        animate_offset=ft.animation.Animation(1000),
    )

    a.content=(c)
    def animate(e):
        c.offset = ft.transform.Offset(0, 0)
        c.update()

    page.add(
        a,
        ft.ElevatedButton("Reveal!", on_click=animate),
    )

ft.app(target=main)