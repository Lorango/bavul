# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:47:29 2018

@author: Lorango
"""

import pygame


class Primitive:
    """Instanca klase.

    """
    def __init__(self, game, rect_arg=(200, 200, 200, 200)):
        """Primitivna inicijalizacija objekta.

        """

        self.game = game

        self.rect = pygame.Rect(rect_arg)

    def draw(self):
        """Primitivno crtanje na ekran.

        """
        # skraćivanje naziva
        surface_input = self.game.surface_input

        # crtanje sebe
        # Nacrtaj pravokutnik. (Najjednostavnije iscrtavanje).
        pygame.draw.rect(surface_input, (250, 50, 250), self.rect)


class Keyboard_input:
    """Instanca klase.

    """

    def K_0(self):
        pass

    def K_1(self):
        pass

    def K_2(self):
        pass

    def K_3(self):
        pass

    def K_4(self):
        pass

    def K_5(self):
        pass

    def K_6(self):
        pass

    def K_7(self):
        pass

    def K_8(self):
        pass

    def K_9(self):
        pass

    def K_AMPERSAND(self):
        pass

    def K_ASTERISK(self):
        pass

    def K_AT(self):
        pass

    def K_BACKQUOTE(self):
        pass

    def K_BACKSLASH(self):
        pass

    def K_BACKSPACE(self):
        pass

    def K_BREAK(self):
        pass

    def K_CAPSLOCK(self):
        pass

    def K_CARET(self):
        pass

    def K_CLEAR(self):
        pass

    def K_COLON(self):
        pass

    def K_COMMA(self):
        pass

    def K_DELETE(self):
        pass

    def K_DOLLAR(self):
        pass

    def K_DOWN(self):
        pass

    def K_END(self):
        pass

    def K_EQUALS(self):
        pass

    def K_ESCAPE(self):
        pass

    def K_EURO(self):
        pass

    def K_EXCLAIM(self):
        pass

    def K_F1(self):
        pass

    def K_F10(self):
        pass

    def K_F11(self):
        pass

    def K_F12(self):
        pass

    def K_F13(self):
        pass

    def K_F14(self):
        pass

    def K_F15(self):
        pass

    def K_F2(self):
        pass

    def K_F3(self):
        pass

    def K_F4(self):
        pass

    def K_F5(self):
        pass

    def K_F6(self):
        pass

    def K_F7(self):
        pass

    def K_F8(self):
        pass

    def K_F9(self):
        pass

    def K_GREATER(self):
        pass

    def K_HASH(self):
        pass

    def K_HELP(self):
        pass

    def K_HOME(self):
        pass

    def K_INSERT(self):
        pass

    def K_KP0(self):
        pass

    def K_KP1(self):
        pass

    def K_KP2(self):
        pass

    def K_KP3(self):
        pass

    def K_KP4(self):
        pass

    def K_KP5(self):
        pass

    def K_KP6(self):
        pass

    def K_KP7(self):
        pass

    def K_KP8(self):
        pass

    def K_KP9(self):
        pass

    def K_KP_DIVIDE(self):
        pass

    def K_KP_ENTER(self):
        pass

    def K_KP_EQUALS(self):
        pass

    def K_KP_MINUS(self):
        pass

    def K_KP_MULTIPLY(self):
        pass

    def K_KP_PERIOD(self):
        pass

    def K_KP_PLUS(self):
        pass

    def K_LALT(self):
        pass

    def K_LCTRL(self):
        pass

    def K_LEFT(self):
        pass

    def K_LEFTBRACKET(self):
        pass

    def K_LEFTPAREN(self):
        pass

    def K_LESS(self):
        pass

    def K_LMETA(self):
        pass

    def K_LSHIFT(self):
        pass

    def K_LSUPER(self):
        pass

    def K_MENU(self):
        pass

    def K_MINUS(self):
        pass

    def K_MODE(self):
        pass

    def K_NUMLOCK(self):
        pass

    def K_PAGEDOWN(self):
        pass

    def K_PAGEUP(self):
        pass

    def K_PAUSE(self):
        pass

    def K_PERIOD(self):
        pass

    def K_PLUS(self):
        pass

    def K_POWER(self):
        pass

    def K_PRINT(self):
        pass

    def K_QUESTION(self):
        pass

    def K_QUOTE(self):
        pass

    def K_QUOTEDBL(self):
        pass

    def K_RALT(self):
        pass

    def K_RCTRL(self):
        pass

    def K_RETURN(self):
        pass

    def K_RIGHT(self):
        pass

    def K_RIGHTBRACKET(self):
        pass

    def K_RIGHTPAREN(self):
        pass

    def K_RMETA(self):
        pass

    def K_RSHIFT(self):
        pass

    def K_RSUPER(self):
        pass

    def K_SCROLLOCK(self):
        pass

    def K_SEMICOLON(self):
        pass

    def K_SLASH(self):
        pass

    def K_SPACE(self):
        pass

    def K_SYSREQ(self):
        pass

    def K_TAB(self):
        pass

    def K_UNDERSCORE(self):
        pass

    def K_UP(self):
        pass

    def K_a(self):
        pass

    def K_b(self):
        pass

    def K_c(self):
        pass

    def K_d(self):
        pass

    def K_e(self):
        pass

    def K_f(self):
        pass

    def K_g(self):
        pass

    def K_h(self):
        pass

    def K_i(self):
        pass

    def K_j(self):
        pass

    def K_k(self):
        pass

    def K_l(self):
        pass

    def K_m(self):
        pass

    def K_n(self):
        pass

    def K_o(self):
        pass

    def K_p(self):
        pass

    def K_q(self):
        pass

    def K_r(self):
        pass

    def K_s(self):
        pass

    def K_t(self):
        pass

    def K_u(self):
        pass

    def K_v(self):
        pass

    def K_w(self):
        pass

    def K_x(self):
        pass

    def K_y(self):
        pass

    def K_z(self):
        pass
