def draw_map():
    tiles = []
    for x in range(dimension):
        for y in range(dimension):
            tiles.append((x, y))
    random.shuffle(tiles)
    pygame.draw.rect(screen, "black", (0, info_panel_height, tile_size * dimension, tile_size * dimension))
    while tiles:
        tile_x = tiles[0][0]
        tile_y = tiles[0][1]
        place = (tile_x * tile_size, tile_y * tile_size + info_panel_height)
        if maze[tile_x][tile_y] == "wall":
            screen.blit(wall_surf, place)
        else:
            screen.blit(tile_surf, place)
            if maze[tile_x][tile_y] == "entrance":
                screen.blit(entrance_surf, place)
            elif maze[tile_x][tile_y] == "exit":
                screen.blit(exit_surf, place)
            elif maze[tile_x][tile_y] == "monster":
                screen.blit(monster_surf, place)
            elif maze[tile_x][tile_y] == "coin":
                screen.blit(coin_surf, place)
            elif maze[tile_x][tile_y] == "health":
                screen.blit(health_surf, place)
            elif maze[tile_x][tile_y] == "treasure":
                screen.blit(treasure_surf, place)
            elif maze[tile_x][tile_y] == "shop":
                screen.blit(shop_surf, place)
            elif maze[tile_x][tile_y] == "in_shop" and player_position != [tile_x, tile_y]:
                screen.blit(shop_surf, place)
                maze[tile_x][tile_y] = "shop"
        pygame.display.update()
        clock.tick(300)
        tiles.pop(0)