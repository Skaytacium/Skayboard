import pcbnew

board = pcbnew.GetBoard()
for drw in board.GetDrawings()
    if drw.IsSelected()
        drw.SetLayer(pcbnew[pcbnew.UserDrawings])
pcbnew.Refresh()