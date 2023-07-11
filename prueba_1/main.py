"""Version de Python utilizada: 3.9.13
by: Paul Vazquez
"""

def count_clean_socks(L:list) -> dict[str,int]:
    """
    Cuenta la cantidad de calcetines limpios por color.

    Args:
        L (list): Lista de colores de calcetines limpios.

    Returns:
        dict: Diccionario donde las claves son los colores de los calcetines y los valores son la cantidad de calcetines de ese color.
    """
    return {sock: L.count(sock) for sock in L}

def count_dirty_socks(S:list) -> dict[str,int]:
    """
    Cuenta la cantidad de calcetines sucios por color.

    Args:
        S (list): Lista de colores de calcetines sucios.

    Returns:
        dict: Diccionario donde las claves son los colores de los calcetines y los valores son la cantidad de calcetines de ese color.
    """
    return {sock: S.count(sock) for sock in S}

def wash_clean_socks(K:int, clean_socks:dict, dirty_socks:dict) -> int:
    """
    Realiza el lavado de los calcetines limpios.

    Args:
        K (int): Máximo número de calcetines que se pueden lavar.
        clean_socks (dict): Diccionario con la cantidad de calcetines limpios por color.
        dirty_socks (dict): Diccionario con la cantidad de calcetines sucios por color.

    Returns:
        int: Número total de pares de calcetines limpios.
    """
    total_pairs = 0

    for color, count in clean_socks.items():
        pairs = count // 2

        if pairs > 0:
            total_pairs += pairs
            clean_socks[color] = count - (pairs * 2)
            dirty_socks[color] = dirty_socks.get(color, 0) + (count % 2)

    return total_pairs

def wash_dirty_socks(K:int, dirty_socks:dict) -> int:
    """
    Realiza el lavado de los calcetines sucios.

    Args:
        K (int): Máximo número de calcetines que se pueden lavar.
        dirty_socks (dict): Diccionario con la cantidad de calcetines sucios por color.

    Returns:
        int: Número total de pares de calcetines limpios.
    """
    total_pairs = 0

    for color, count in dirty_socks.items():
        pairs = min(count // 2, K)

        if pairs > 0:
            total_pairs += pairs
            dirty_socks[color] = count - (pairs * 2)

    return total_pairs

def solucion(K:int, L:list, S:list) -> int:
    """
    Calcula el máximo número de pares de calcetines que Pedro puede llevar en su viaje.

    Args:
        K (int): Máximo número de calcetines que se pueden lavar.
        L (list): Lista de colores de calcetines limpios.
        S (list): Lista de colores de calcetines sucios.

    Returns:
        int: Número total de pares de calcetines limpios que Pedro puede llevar en su viaje.
    """
    clean_socks = count_clean_socks(L)
    dirty_socks = count_dirty_socks(S)

    total_pairs = wash_clean_socks(K, clean_socks, dirty_socks)
    total_pairs += wash_dirty_socks(K, dirty_socks)

    return total_pairs

if __name__ == "__main__":
    print(solucion(2, [1, 2, 1, 1], [1, 4, 3, 2, 4]))
