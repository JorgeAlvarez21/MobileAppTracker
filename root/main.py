
import flet as ft
import datetime as dt
import calendar
import asyncio
import time
import routing
import add_task as taskControls

def main(page: ft.page):
    page.window_height = 900
    page.window_width = 460
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = '#35363c'
    page.theme_mode = 'light'
    # Routing functions
    _route = routing.PaginationRouting()

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

    # **********************************************  Home View **********************************************
    _body_base = ft.Container(expand=True, border_radius=ft.border_radius.all(30))
    _body_home = ft.Column(alignment=ft.MainAxisAlignment("start"), spacing=0)
    _body_main.controls.append(_body_base)

    _top_bar = ft.Stack(controls=[
        ft.Container(padding=ft.padding.only(top=30, bottom=5), height=130, content=ft.Row(controls=[
            ft.Container(expand=False, margin=ft.margin.only(left=20, right=10),
                         content=ft.Image('/fake-prof.jpg', width=50, height=50,
                                          border_radius=ft.border_radius.all(100))),
            ft.Text('Lorem Ipsum', color=ft.colors.BLACK, size=14)]))])

    def day_cards():
        card_controls = []
        for day in range(-3, 4):
            day = today + dt.timedelta(day)
            c = ft.Container(data=day, width=43, height=65, border_radius=ft.border_radius.all(15),
                             padding=ft.padding.only(top=5), bgcolor='#bce4ff',
                             alignment=ft.alignment.center, on_hover= lambda e: card_day_hover(e), on_click = lambda e: card_day_select(e),
                             content=ft.Column(spacing=2, horizontal_alignment=ft.CrossAxisAlignment('center'),
                                               controls=[
                                                   ft.Text(day.strftime('%a'), weight='w100', size=14,
                                                           color=ft.colors.BLACK),
                                                   ft.Text(day.strftime('%-d'), color=ft.colors.BLACK)]))
            if c.data.day == today.day:
                c.bgcolor = ft.colors.BLACK
                c.content.controls[0].color = ft.colors.WHITE
                c.content.controls[1].color = ft.colors.WHITE
            card_controls.append(c)
        return card_controls

    def generate_calendar(month=None, year=None):
        if not year: year = today.year
        if not month: month = today.month

        num_days = calendar.monthrange(year, month)[1]
        days = [dt.date(year, month, day) for day in range(1, num_days + 1)]
        months_row = ft.Row(width=340, wrap=True, spacing=9, run_spacing=10,
                            vertical_alignment=ft.CrossAxisAlignment('center'),
                            alignment=ft.MainAxisAlignment('center'), controls=[])
        days_abbr = [calendar.day_abbr[x] for x in range(0, 7)]
        days_abbr.insert(0, days_abbr.pop(-1))
        d_days = {k: v for (v, k) in enumerate(days_abbr)}
        first = d_days.get(calendar.day_abbr[days[0].weekday()])

        months_row.controls.append(
            ft.Row(width=340, wrap=True, spacing=9, run_spacing=9, vertical_alignment=ft.CrossAxisAlignment('center'),
                   alignment=ft.MainAxisAlignment('center'),
                   controls=[ft.Container(alignment=ft.alignment.center, width=36, height=36,
                                          content=ft.Text(x, color=ft.colors.BLACK)) for x in days_abbr]))
        count = 0
        for i, d in enumerate(range(35)):
            if i >= first and i < num_days + first:
                d = days[0 + count]

                day_c = ft.Container(data=False, on_click=lambda e: card_day_select_expanded(e), border_radius=ft.border_radius.all(10), width=36, height=36,
                                     border=ft.border.all(.5, color=ft.colors.BLACK), bgcolor='#bce4ff', on_hover= lambda e: card_day_hover(e),
                                     content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment('center'),
                                                       alignment=ft.MainAxisAlignment('center'),
                                                       controls=[ft.Text(d.day, color=ft.colors.BLACK)]))
                if d.day == today.day:
                    day_c.bgcolor = ft.colors.BLACK
                    day_c.content.controls[0].color = ft.colors.WHITE
                count += 1
            else:
                day_c = ft.Container(border_radius=ft.border_radius.all(10), width=36, height=36,
                                     border=ft.border.all(.5, color=ft.colors.BLACK),
                                     content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment('center'),
                                                       alignment=ft.MainAxisAlignment('center'), controls=[]))

            months_row.controls.append(day_c)
        return months_row


    def card_day_hover(e):
        if e.control.bgcolor != ft.colors.BLACK:
            if e.data == 'true':
                e.control.bgcolor = ft.colors.BLUE_50
            else:
                e.control.bgcolor = '#bce4ff'
            e.control.update()

    def card_day_select_expanded(e):
        print('trisert')
        e.control.bgcolor = ft.colors.BLACK
        e.control.content.controls[0].color = ft.colors.WHITE
        e.control.update()
        pass

    def card_day_select(e):
        e.control.bgcolor = ft.colors.BLACK
        e.control.content.controls[0].color = ft.colors.WHITE
        e.control.content.controls[1].color = ft.colors.WHITE

        e.control.update()
        pass
    def calendar_expanded(e):
        if _calendar.height == 120:
            _calendar.height = 320
            # Expands here

            week_cards.visible = False
            _months = generate_calendar()
            # Adds the calendar
            _calendar.content.controls.extend([_months])

        else:
            # Remove the calendar
            _calendar.content.controls.pop()
            _calendar.height = 120
            week_cards.visible = True
        page.update()

    week_cards = ft.Row(spacing=7, alignment=ft.MainAxisAlignment('center'), controls=day_cards())

    _calendar = ft.Container(height=120, content=
    ft.Column(expand=True, spacing=0, alignment=ft.MainAxisAlignment('start'),
              horizontal_alignment=ft.CrossAxisAlignment('center'),
              controls=[ft.Row(alignment=ft.MainAxisAlignment('center'), spacing=0, controls=[
                  ft.Container(margin=ft.margin.only(bottom=10),
                               content=ft.Text(today.strftime("%B"), size=22, weight='w500', color=ft.colors.BLACK)),
                  ft.Container(margin=ft.margin.only(bottom=5),
                               content=ft.IconButton("ARROW_DROP_DOWN", icon_size=22, icon_color=ft.colors.BLACK,
                                                     on_click=calendar_expanded))]),
                        week_cards
                        ]))
    _habits_msg = ft.Container(margin=ft.margin.only(left=20, bottom=10), height=35,
                               content=ft.Text('My Habits', size=22, weight='w500', color=ft.colors.BLACK))

    _cards = ft.Container(expand=1,
                          content=ft.Column(spacing=20, expand=1, width=393,
                                            horizontal_alignment=ft.CrossAxisAlignment('center'),
                                            alignment=ft.MainAxisAlignment('start'),
                                            wrap=False, scroll=ft.ScrollMode.ADAPTIVE, controls=[
                                  ft.ElevatedButton(elevation=3, height=90, width=330, bgcolor='#F3F3F3', disabled=True,
                                                    style=ft.ButtonStyle(
                                                        shape={'': ft.buttons.RoundedRectangleBorder(radius=10)}),
                                                    content=ft.Container(
                                                        content=ft.Column(wrap=False, spacing=0, expand=True, controls=[
                                                            ft.Container(height=30,
                                                                         alignment=ft.alignment.top_center,
                                                                         content=ft.Text('Morning Run', size=20,
                                                                                         color=ft.colors.BLACK)),
                                                            ft.Row(spacing=23, height=40, controls=[
                                                                ft.Container(margin=ft.margin.only(left=30), width=35,
                                                                             height=35,
                                                                             content=ft.Image('/fake-profile1.jpeg',
                                                                                              border_radius=ft.border_radius.all(
                                                                                                  100), expand=True)),

                                                                ft.Container(content=ft.Text('3 mi - Mon, Thu',
                                                                                             color=ft.colors.BLACK))]),
                                                            ft.Container(expand=False,
                                                                         border_radius=ft.border_radius.all(20),
                                                                         offset=ft.transform.Offset(x=0, y=.27),
                                                                         scale=ft.transform.Scale(scale_x=1.105,
                                                                                                  scale_y=1.05),
                                                                         height=15, width=380, bgcolor='#bce4ff',
                                                                         margin=ft.margin.all(0),
                                                                         padding=ft.padding.all(0),
                                                                         alignment=ft.alignment.top_left,
                                                                         content=ft.Container(expand=False,
                                                                                              border_radius=ft.border_radius.all(
                                                                                                  20), height=20,
                                                                                              width=330,
                                                                                              bgcolor=ft.colors.LIGHT_BLUE_500,
                                                                                              scale=ft.transform.Scale(
                                                                                                  scale_x=.5),
                                                                                              offset=ft.transform.Offset(
                                                                                                  -.25, 0)))
                                                            # Scale will be the progress and the offset will be scale/2
                                                        ])
                                                    )),
                                  ft.ElevatedButton(elevation=3, height=90, width=330, bgcolor='#F3F3F3', disabled=True,
                                                    style=ft.ButtonStyle(
                                                        shape={'': ft.buttons.RoundedRectangleBorder(radius=10)}),
                                                    content=ft.Container(
                                                    )),
                                  ft.ElevatedButton(elevation=3, height=90, width=330, bgcolor='#F3F3F3', disabled=True,
                                                    style=ft.ButtonStyle(
                                                        shape={'': ft.buttons.RoundedRectangleBorder(radius=10)}),
                                                    content=ft.Container(
                                                    )),
                                  ft.ElevatedButton(elevation=3, height=90, width=330, bgcolor='#F3F3F3', disabled=True,
                                                    style=ft.ButtonStyle(
                                                        shape={'': ft.buttons.RoundedRectangleBorder(radius=10)}),
                                                    content=ft.Container(
                                                    )),
                                  ft.ElevatedButton(elevation=3, height=90, width=330, bgcolor='#F3F3F3', disabled=True,
                                                    style=ft.ButtonStyle(
                                                        shape={'': ft.buttons.RoundedRectangleBorder(radius=10)}),
                                                    content=ft.Container(
                                                    )),
                                  ft.Container(height=10, width=330),
                              ]))

    # **********************************************  Add Task View **********************************************

    _add_task_base = ft.Container(expand=True, border_radius=ft.border_radius.all(30))
    _add_task_content = ft.Container(height=760, width=page.width, bgcolor=ft.colors.WHITE,
                                     gradient=ft.LinearGradient(begin=ft.alignment.top_center,
                                                                end=ft.alignment.bottom_center,
                                                                colors=['#cdebff', ft.colors.WHITE]), border_radius=10,
                                     offset=ft.transform.Offset(0, .90),
                                     scale=ft.transform.Scale(1, 1),
                                     animate_offset = ft.Animation(800, curve=ft.AnimationCurve.EASE_IN),
                                     animate_scale = ft.Animation(10))
    _body_add_task = ft.Column(expand=True, controls=[])

    _close_btn = ft.Container(height=40, margin=ft.margin.only(top=20), padding=ft.padding.only(left=10),
                              content=ft.Row(spacing=4, controls=[
                                  ft.IconButton(ft.icons.CLOSE, on_click=lambda e: close_task_view(e)),
                                  # ft.Text('CLOSE'),
                                  ft.Container(expand=True, alignment=ft.alignment.center_right,
                                               padding=ft.padding.only(right=10),
                                               content=ft.IconButton(ft.icons.REFRESH))
                              ]))

    # Views Controllers
    view_active = ['home', 'add_task']


    def check_route(e):
        _route.viewAllRoutes()

    def home_view(e):
        _route.viewAllRoutes()
        if str(_route.node_head) != 'home':
            _route.goBackToInitial()

        _body_base.content = _body_home
        _body_home.controls.clear()
        _body_home.controls.append(_top_bar)
        _body_home.controls.append(_calendar)
        _body_home.controls.append(_habits_msg)
        _body_home.controls.append(_cards)
        page.update()

    def task_view(e):
        print(_route.node_head.name)
        if _route.node_head.name != 'add_task':
            _route.addRoute('add_task')
            _route.viewAllRoutes()
            _body_main.controls.append(_add_task_base)
            _add_task_base.content = _add_task_content
            _add_task_content.content = _body_add_task
            _body_add_task.controls.clear()
            _name_bar = taskControls.ControllerNameBar()
            _select_day =taskControls.ControllerSelectDay()
            _set_reminder = taskControls.ControllerReminder()
            _set_repeat =taskControls.ControllerRepeat()
            _set_daterange =taskControls.ControllerDateRange()
            _set_goal =taskControls.ControllerSetGoal()
            _set_comment =taskControls.ControllerSetCommet()
            _submit_btn =taskControls.ControllerSubmitBtn()
            controls = [_close_btn, _name_bar, _select_day, _set_reminder, _set_repeat, _set_daterange, _set_goal,
                        _set_comment, _submit_btn]

            _body_add_task.controls.extend(controls
                )
            page.update()
            time.sleep(.02)
            AnimationFuncs.animated_view_slideup()
            time.sleep(.09)
            _add_task_base.content.update()
            # Adding content



    def close_task_view(e):
        _route.viewAllRoutes()
        _route.popRoute()
        _route.viewAllRoutes()

        AnimationFuncs.animated_view_slidedown()
        _add_task_base.update()
        time.sleep(.9)
        _body_main.controls.pop()
        page.update()


    class AnimationFuncs:
        """ Animation Functions and other helper tools for pagination and other """

        # View Slides
        def animated_view_slideup():
            _add_task_content.offset = ft.transform.Offset(0, 0)
            _add_task_content.scale = ft.transform.Scale(1, 1)
            _add_task_content.update()

        def animated_view_slidedown():
            _add_task_content.scale = ft.transform.Scale(1, 1, 0)
            _add_task_content.offset = ft.transform.Offset(0, 1)

            _add_task_content.update()

    page.add(_device)


ft.app(target=main, assets_dir="../media")
