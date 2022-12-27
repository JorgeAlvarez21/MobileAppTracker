import flet as ft
import datetime as dt


def main(page: ft.page):
    page.window_height = 900
    page.window_width = 460
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = '#35363c'
    page.theme_mode = 'light'

    # Variables
    device_height = 852
    device_width = 393
    body_height = 760
    today = dt.datetime.now()
    # ********************************************  Main Screen Layout ********************************************

    _device = ft.Stack(controls=[])
    _main = ft.Container(height=device_height, width=device_width, bgcolor=ft.colors.WHITE,
                         gradient=ft.LinearGradient(begin=ft.alignment.top_center,
                                                    end=ft.alignment.bottom_center,
                                                    colors=['#cdebff', ft.colors.WHITE]),
                         border_radius=ft.border_radius.all(30),
                         border=ft.border.all(10, ft.colors.BLACK))
    _device.controls.append(_main)
    _main_layout = ft.Column(spacing=0, controls=[])

    _body_main = ft.Stack(height=body_height, width=device_width, controls=[])

    _footer = ft.Container(expand=True, border_radius=ft.border_radius.all(30))
    _device_details = ft.Container(
        content=ft.Container(height=35, width=130, bgcolor=ft.colors.BLACK,
                             border_radius=ft.border_radius.all(15),
                             offset=ft.transform.Offset(1, 0)))
    _device.controls.append(_device_details)

    _main.content = _main_layout
    _main_layout.controls.extend([_body_main, _footer])
    _menubar = ft.Container(expand=True, bgcolor=ft.colors.BLACK, border_radius=ft.border_radius.all(30),
                            margin=ft.margin.only(left=5, right=5, top=5, bottom=10),
                            content=ft.Row(spacing=10, alignment=ft.MainAxisAlignment('spaceEvenly'), controls=[
                                ft.IconButton(icon=ft.icons.HOME_ROUNDED, icon_size=30,
                                              on_click=lambda e: home_view(e)),
                                ft.IconButton(icon=ft.icons.CALENDAR_TODAY, icon_size=25),
                                ft.Container(bgcolor=ft.colors.BLACK, offset=ft.transform.Offset(0, -.25), height=65,
                                             width=65, border_radius=ft.border_radius.all(100),
                                             content=ft.Container(height=55, width=55,
                                                                  alignment=ft.alignment.center,
                                                                  margin=ft.margin.only(top=10),
                                                                  border_radius=ft.border_radius.all(100), content=
                                                                  ft.IconButton(icon=ft.icons.ADD, icon_size=25,
                                                                                bgcolor=ft.colors.LIGHT_BLUE,
                                                                                on_click=lambda e: task_view(
                                                                                    e)))),
                                ft.IconButton(icon=ft.icons.INSIGHTS, icon_size=25, on_click=lambda e: check_route(e)),
                                ft.IconButton(icon=ft.icons.SETTINGS, icon_size=25),
                            ]))
    _footer.content = _menubar

    # **********************************************  Add Task View **********************************************

    _add_task_base = ft.Container(expand=True, border_radius=ft.border_radius.all(30))
    _add_task_content = ft.Container(height=760, width=page.width, bgcolor=ft.colors.WHITE,
                                     gradient=ft.LinearGradient(begin=ft.alignment.top_center,
                                                                end=ft.alignment.bottom_center,
                                                                colors=['#b9d8e8', ft.colors.WHITE]), border_radius=15,
                                     animate_offset=ft.Animation(800, curve=ft.AnimationCurve.EASE_IN),
                                     animate_scale=ft.Animation(10))
    _body_add_task = ft.Column(spacing=0, expand=True, controls=[])

    _main_icon = ft.Container(height=400, margin=ft.margin.only(right=20, top=20), padding=ft.padding.only(top=50), alignment=ft.alignment.center, content=ft.Image('bike-riding.png', width=280, height=300))

    _text_welcome = ft.Container(height=100, alignment=ft.alignment.center, content=ft.Text('Welcome', size=38, weight='w500'))

    _button_slide = ft.Container(height=250, padding=ft.padding.only(bottom=90), alignment=ft.alignment.center, content=ft.IconButton(ft.icons.ARROW_FORWARD, icon_size=80, bgcolor=ft.colors.BLUE_GREY_200))


    _body_main.controls.append(_add_task_base)
    _add_task_base.content = _add_task_content
    _add_task_content.content = _body_add_task
    _body_add_task.controls.extend(
        [_main_icon, _text_welcome, _button_slide])
    page.add(_device)
    page.update()


ft.app(target=main, assets_dir="../media")
