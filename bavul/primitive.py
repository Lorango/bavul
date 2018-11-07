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


class Key_down:
    """Instanca klase.

    """

    def K_0_down(self):
        pass

    def K_1_down(self):
        pass

    def K_2_down(self):
        pass

    def K_3_down(self):
        pass

    def K_4_down(self):
        pass

    def K_5_down(self):
        pass

    def K_6_down(self):
        pass

    def K_7_down(self):
        pass

    def K_8_down(self):
        pass

    def K_9_down(self):
        pass

    def K_AMPERSAND_down(self):
        pass

    def K_ASTERISK_down(self):
        pass

    def K_AT_down(self):
        pass

    def K_BACKQUOTE_down(self):
        pass

    def K_BACKSLASH_down(self):
        pass

    def K_BACKSPACE_down(self):
        pass

    def K_BREAK_down(self):
        pass

    def K_CAPSLOCK_down(self):
        pass

    def K_CARET_down(self):
        pass

    def K_CLEAR_down(self):
        pass

    def K_COLON_down(self):
        pass

    def K_COMMA_down(self):
        pass

    def K_DELETE_down(self):
        pass

    def K_DOLLAR_down(self):
        pass

    def K_DOWN_down(self):
        pass

    def K_END_down(self):
        pass

    def K_EQUALS_down(self):
        pass

    def K_ESCAPE_down(self):
        pass

    def K_EURO_down(self):
        pass

    def K_EXCLAIM_down(self):
        pass

    def K_F1_down(self):
        pass

    def K_F10_down(self):
        pass

    def K_F11_down(self):
        pass

    def K_F12_down(self):
        pass

    def K_F13_down(self):
        pass

    def K_F14_down(self):
        pass

    def K_F15_down(self):
        pass

    def K_F2_down(self):
        pass

    def K_F3_down(self):
        pass

    def K_F4_down(self):
        pass

    def K_F5_down(self):
        pass

    def K_F6_down(self):
        pass

    def K_F7_down(self):
        pass

    def K_F8_down(self):
        pass

    def K_F9_down(self):
        pass

    def K_GREATER_down(self):
        pass

    def K_HASH_down(self):
        pass

    def K_HELP_down(self):
        pass

    def K_HOME_down(self):
        pass

    def K_INSERT_down(self):
        pass

    def K_KP0_down(self):
        pass

    def K_KP1_down(self):
        pass

    def K_KP2_down(self):
        pass

    def K_KP3_down(self):
        pass

    def K_KP4_down(self):
        pass

    def K_KP5_down(self):
        pass

    def K_KP6_down(self):
        pass

    def K_KP7_down(self):
        pass

    def K_KP8_down(self):
        pass

    def K_KP9_down(self):
        pass

    def K_KP_DIVIDE_down(self):
        pass

    def K_KP_ENTER_down(self):
        pass

    def K_KP_EQUALS_down(self):
        pass

    def K_KP_MINUS_down(self):
        pass

    def K_KP_MULTIPLY_down(self):
        pass

    def K_KP_PERIOD_down(self):
        pass

    def K_KP_PLUS_down(self):
        pass

    def K_LALT_down(self):
        pass

    def K_LCTRL_down(self):
        pass

    def K_LEFT_down(self):
        pass

    def K_LEFTBRACKET_down(self):
        pass

    def K_LEFTPAREN_down(self):
        pass

    def K_LESS_down(self):
        pass

    def K_LMETA_down(self):
        pass

    def K_LSHIFT_down(self):
        pass

    def K_LSUPER_down(self):
        pass

    def K_MENU_down(self):
        pass

    def K_MINUS_down(self):
        pass

    def K_MODE_down(self):
        pass

    def K_NUMLOCK_down(self):
        pass

    def K_PAGEDOWN_down(self):
        pass

    def K_PAGEUP_down(self):
        pass

    def K_PAUSE_down(self):
        pass

    def K_PERIOD_down(self):
        pass

    def K_PLUS_down(self):
        pass

    def K_POWER_down(self):
        pass

    def K_PRINT_down(self):
        pass

    def K_QUESTION_down(self):
        pass

    def K_QUOTE_down(self):
        pass

    def K_QUOTEDBL_down(self):
        pass

    def K_RALT_down(self):
        pass

    def K_RCTRL_down(self):
        pass

    def K_RETURN_down(self):
        pass

    def K_RIGHT_down(self):
        pass

    def K_RIGHTBRACKET_down(self):
        pass

    def K_RIGHTPAREN_down(self):
        pass

    def K_RMETA_down(self):
        pass

    def K_RSHIFT_down(self):
        pass

    def K_RSUPER_down(self):
        pass

    def K_SCROLLOCK_down(self):
        pass

    def K_SEMICOLON_down(self):
        pass

    def K_SLASH_down(self):
        pass

    def K_SPACE_down(self):
        pass

    def K_SYSREQ_down(self):
        pass

    def K_TAB_down(self):
        pass

    def K_UNDERSCORE_down(self):
        pass

    def K_UP_down(self):
        pass

    def K_a_down(self):
        pass

    def K_b_down(self):
        pass

    def K_c_down(self):
        pass

    def K_d_down(self):
        pass

    def K_e_down(self):
        pass

    def K_f_down(self):
        pass

    def K_g_down(self):
        pass

    def K_h_down(self):
        pass

    def K_i_down(self):
        pass

    def K_j_down(self):
        pass

    def K_k_down(self):
        pass

    def K_l_down(self):
        pass

    def K_m_down(self):
        pass

    def K_n_down(self):
        pass

    def K_o_down(self):
        pass

    def K_p_down(self):
        pass

    def K_q_down(self):
        pass

    def K_r_down(self):
        pass

    def K_s_down(self):
        pass

    def K_t_down(self):
        pass

    def K_u_down(self):
        pass

    def K_v_down(self):
        pass

    def K_w_down(self):
        pass

    def K_x_down(self):
        pass

    def K_y_down(self):
        pass

    def K_z_down(self):
        pass


class Key_up:
    """Instanca klase.

    """

    def K_0_up(self):
        pass

    def K_1_up(self):
        pass

    def K_2_up(self):
        pass

    def K_3_up(self):
        pass

    def K_4_up(self):
        pass

    def K_5_up(self):
        pass

    def K_6_up(self):
        pass

    def K_7_up(self):
        pass

    def K_8_up(self):
        pass

    def K_9_up(self):
        pass

    def K_AMPERSAND_up(self):
        pass

    def K_ASTERISK_up(self):
        pass

    def K_AT_up(self):
        pass

    def K_BACKQUOTE_up(self):
        pass

    def K_BACKSLASH_up(self):
        pass

    def K_BACKSPACE_up(self):
        pass

    def K_BREAK_up(self):
        pass

    def K_CAPSLOCK_up(self):
        pass

    def K_CARET_up(self):
        pass

    def K_CLEAR_up(self):
        pass

    def K_COLON_up(self):
        pass

    def K_COMMA_up(self):
        pass

    def K_DELETE_up(self):
        pass

    def K_DOLLAR_up(self):
        pass

    def K_DOWN_up(self):
        pass

    def K_END_up(self):
        pass

    def K_EQUALS_up(self):
        pass

    def K_ESCAPE_up(self):
        pass

    def K_EURO_up(self):
        pass

    def K_EXCLAIM_up(self):
        pass

    def K_F1_up(self):
        pass

    def K_F10_up(self):
        pass

    def K_F11_up(self):
        pass

    def K_F12_up(self):
        pass

    def K_F13_up(self):
        pass

    def K_F14_up(self):
        pass

    def K_F15_up(self):
        pass

    def K_F2_up(self):
        pass

    def K_F3_up(self):
        pass

    def K_F4_up(self):
        pass

    def K_F5_up(self):
        pass

    def K_F6_up(self):
        pass

    def K_F7_up(self):
        pass

    def K_F8_up(self):
        pass

    def K_F9_up(self):
        pass

    def K_GREATER_up(self):
        pass

    def K_HASH_up(self):
        pass

    def K_HELP_up(self):
        pass

    def K_HOME_up(self):
        pass

    def K_INSERT_up(self):
        pass

    def K_KP0_up(self):
        pass

    def K_KP1_up(self):
        pass

    def K_KP2_up(self):
        pass

    def K_KP3_up(self):
        pass

    def K_KP4_up(self):
        pass

    def K_KP5_up(self):
        pass

    def K_KP6_up(self):
        pass

    def K_KP7_up(self):
        pass

    def K_KP8_up(self):
        pass

    def K_KP9_up(self):
        pass

    def K_KP_DIVIDE_up(self):
        pass

    def K_KP_ENTER_up(self):
        pass

    def K_KP_EQUALS_up(self):
        pass

    def K_KP_MINUS_up(self):
        pass

    def K_KP_MULTIPLY_up(self):
        pass

    def K_KP_PERIOD_up(self):
        pass

    def K_KP_PLUS_up(self):
        pass

    def K_LALT_up(self):
        pass

    def K_LCTRL_up(self):
        pass

    def K_LEFT_up(self):
        pass

    def K_LEFTBRACKET_up(self):
        pass

    def K_LEFTPAREN_up(self):
        pass

    def K_LESS_up(self):
        pass

    def K_LMETA_up(self):
        pass

    def K_LSHIFT_up(self):
        pass

    def K_LSUPER_up(self):
        pass

    def K_MENU_up(self):
        pass

    def K_MINUS_up(self):
        pass

    def K_MODE_up(self):
        pass

    def K_NUMLOCK_up(self):
        pass

    def K_PAGEDOWN_up(self):
        pass

    def K_PAGEUP_up(self):
        pass

    def K_PAUSE_up(self):
        pass

    def K_PERIOD_up(self):
        pass

    def K_PLUS_up(self):
        pass

    def K_POWER_up(self):
        pass

    def K_PRINT_up(self):
        pass

    def K_QUESTION_up(self):
        pass

    def K_QUOTE_up(self):
        pass

    def K_QUOTEDBL_up(self):
        pass

    def K_RALT_up(self):
        pass

    def K_RCTRL_up(self):
        pass

    def K_RETURN_up(self):
        pass

    def K_RIGHT_up(self):
        pass

    def K_RIGHTBRACKET_up(self):
        pass

    def K_RIGHTPAREN_up(self):
        pass

    def K_RMETA_up(self):
        pass

    def K_RSHIFT_up(self):
        pass

    def K_RSUPER_up(self):
        pass

    def K_SCROLLOCK_up(self):
        pass

    def K_SEMICOLON_up(self):
        pass

    def K_SLASH_up(self):
        pass

    def K_SPACE_up(self):
        pass

    def K_SYSREQ_up(self):
        pass

    def K_TAB_up(self):
        pass

    def K_UNDERSCORE_up(self):
        pass

    def K_UP_up(self):
        pass

    def K_a_up(self):
        pass

    def K_b_up(self):
        pass

    def K_c_up(self):
        pass

    def K_d_up(self):
        pass

    def K_e_up(self):
        pass

    def K_f_up(self):
        pass

    def K_g_up(self):
        pass

    def K_h_up(self):
        pass

    def K_i_up(self):
        pass

    def K_j_up(self):
        pass

    def K_k_up(self):
        pass

    def K_l_up(self):
        pass

    def K_m_up(self):
        pass

    def K_n_up(self):
        pass

    def K_o_up(self):
        pass

    def K_p_up(self):
        pass

    def K_q_up(self):
        pass

    def K_r_up(self):
        pass

    def K_s_up(self):
        pass

    def K_t_up(self):
        pass

    def K_u_up(self):
        pass

    def K_v_up(self):
        pass

    def K_w_up(self):
        pass

    def K_x_up(self):
        pass

    def K_y_up(self):
        pass

    def K_z_up(self):
        pass


class Key_pressed:
    """Instanca klase.

    """

    def K_0_pressed(self):
        pass

    def K_1_pressed(self):
        pass

    def K_2_pressed(self):
        pass

    def K_3_pressed(self):
        pass

    def K_4_pressed(self):
        pass

    def K_5_pressed(self):
        pass

    def K_6_pressed(self):
        pass

    def K_7_pressed(self):
        pass

    def K_8_pressed(self):
        pass

    def K_9_pressed(self):
        pass

    def K_AMPERSAND_pressed(self):
        pass

    def K_ASTERISK_pressed(self):
        pass

    def K_AT_pressed(self):
        pass

    def K_BACKQUOTE_pressed(self):
        pass

    def K_BACKSLASH_pressed(self):
        pass

    def K_BACKSPACE_pressed(self):
        pass

    def K_BREAK_pressed(self):
        pass

    def K_CAPSLOCK_pressed(self):
        pass

    def K_CARET_pressed(self):
        pass

    def K_CLEAR_pressed(self):
        pass

    def K_COLON_pressed(self):
        pass

    def K_COMMA_pressed(self):
        pass

    def K_DELETE_pressed(self):
        pass

    def K_DOLLAR_pressed(self):
        pass

    def K_DOWN_pressed(self):
        pass

    def K_END_pressed(self):
        pass

    def K_EQUALS_pressed(self):
        pass

    def K_ESCAPE_pressed(self):
        pass

    def K_EURO_pressed(self):
        pass

    def K_EXCLAIM_pressed(self):
        pass

    def K_F1_pressed(self):
        pass

    def K_F10_pressed(self):
        pass

    def K_F11_pressed(self):
        pass

    def K_F12_pressed(self):
        pass

    def K_F13_pressed(self):
        pass

    def K_F14_pressed(self):
        pass

    def K_F15_pressed(self):
        pass

    def K_F2_pressed(self):
        pass

    def K_F3_pressed(self):
        pass

    def K_F4_pressed(self):
        pass

    def K_F5_pressed(self):
        pass

    def K_F6_pressed(self):
        pass

    def K_F7_pressed(self):
        pass

    def K_F8_pressed(self):
        pass

    def K_F9_pressed(self):
        pass

    def K_GREATER_pressed(self):
        pass

    def K_HASH_pressed(self):
        pass

    def K_HELP_pressed(self):
        pass

    def K_HOME_pressed(self):
        pass

    def K_INSERT_pressed(self):
        pass

    def K_KP0_pressed(self):
        pass

    def K_KP1_pressed(self):
        pass

    def K_KP2_pressed(self):
        pass

    def K_KP3_pressed(self):
        pass

    def K_KP4_pressed(self):
        pass

    def K_KP5_pressed(self):
        pass

    def K_KP6_pressed(self):
        pass

    def K_KP7_pressed(self):
        pass

    def K_KP8_pressed(self):
        pass

    def K_KP9_pressed(self):
        pass

    def K_KP_DIVIDE_pressed(self):
        pass

    def K_KP_ENTER_pressed(self):
        pass

    def K_KP_EQUALS_pressed(self):
        pass

    def K_KP_MINUS_pressed(self):
        pass

    def K_KP_MULTIPLY_pressed(self):
        pass

    def K_KP_PERIOD_pressed(self):
        pass

    def K_KP_PLUS_pressed(self):
        pass

    def K_LALT_pressed(self):
        pass

    def K_LCTRL_pressed(self):
        pass

    def K_LEFT_pressed(self):
        pass

    def K_LEFTBRACKET_pressed(self):
        pass

    def K_LEFTPAREN_pressed(self):
        pass

    def K_LESS_pressed(self):
        pass

    def K_LMETA_pressed(self):
        pass

    def K_LSHIFT_pressed(self):
        pass

    def K_LSUPER_pressed(self):
        pass

    def K_MENU_pressed(self):
        pass

    def K_MINUS_pressed(self):
        pass

    def K_MODE_pressed(self):
        pass

    def K_NUMLOCK_pressed(self):
        pass

    def K_PAGEDOWN_pressed(self):
        pass

    def K_PAGEUP_pressed(self):
        pass

    def K_PAUSE_pressed(self):
        pass

    def K_PERIOD_pressed(self):
        pass

    def K_PLUS_pressed(self):
        pass

    def K_POWER_pressed(self):
        pass

    def K_PRINT_pressed(self):
        pass

    def K_QUESTION_pressed(self):
        pass

    def K_QUOTE_pressed(self):
        pass

    def K_QUOTEDBL_pressed(self):
        pass

    def K_RALT_pressed(self):
        pass

    def K_RCTRL_pressed(self):
        pass

    def K_RETURN_pressed(self):
        pass

    def K_RIGHT_pressed(self):
        pass

    def K_RIGHTBRACKET_pressed(self):
        pass

    def K_RIGHTPAREN_pressed(self):
        pass

    def K_RMETA_pressed(self):
        pass

    def K_RSHIFT_pressed(self):
        pass

    def K_RSUPER_pressed(self):
        pass

    def K_SCROLLOCK_pressed(self):
        pass

    def K_SEMICOLON_pressed(self):
        pass

    def K_SLASH_pressed(self):
        pass

    def K_SPACE_pressed(self):
        pass

    def K_SYSREQ_pressed(self):
        pass

    def K_TAB_pressed(self):
        pass

    def K_UNDERSCORE_pressed(self):
        pass

    def K_UP_pressed(self):
        pass

    def K_a_pressed(self):
        pass

    def K_b_pressed(self):
        pass

    def K_c_pressed(self):
        pass

    def K_d_pressed(self):
        pass

    def K_e_pressed(self):
        pass

    def K_f_pressed(self):
        pass

    def K_g_pressed(self):
        pass

    def K_h_pressed(self):
        pass

    def K_i_pressed(self):
        pass

    def K_j_pressed(self):
        pass

    def K_k_pressed(self):
        pass

    def K_l_pressed(self):
        pass

    def K_m_pressed(self):
        pass

    def K_n_pressed(self):
        pass

    def K_o_pressed(self):
        pass

    def K_p_pressed(self):
        pass

    def K_q_pressed(self):
        pass

    def K_r_pressed(self):
        pass

    def K_s_pressed(self):
        pass

    def K_t_pressed(self):
        pass

    def K_u_pressed(self):
        pass

    def K_v_pressed(self):
        pass

    def K_w_pressed(self):
        pass

    def K_x_pressed(self):
        pass

    def K_y_pressed(self):
        pass

    def K_z_pressed(self):
        pass
