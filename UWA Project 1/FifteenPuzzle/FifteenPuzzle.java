
/**
 * Write a description of class FifteenPuzzle here.
 * 
 * @author Jai Castle
 * @version 7th May 2018
 */

import java.awt.event.*;
import java.awt.Color;
import java.util.Random;
import java.util.concurrent.TimeUnit;
import java.util.Arrays;

public class FifteenPuzzle implements MouseListener
{ 
    private int[][] grid; // the current positions of the tiles and space, denoted by 0..15
    private int xspace;   // xspace,yspace are the current coordinates of the space
    private int yspace;
    private SimpleCanvas sc; // the canvas for display
     
    private final int size     = 4;               // the number of tiles across and down 
    private final int tilesize = 50;              // the size of a tile
    private final int gridsize = size * tilesize; // the size of the grid 
    
    private        int[][] goal    = {{1, 5,9,13}, {2,6,10,14}, {3,7,11,15}, {4,8,12, 0}};
    // these two are public so that they can be used in BlueJ 
    public  static int[][] close   = {{1, 5,9,13}, {2,6,10,14}, {3,7,11, 0}, {4,8,12,15}};
    public  static int[][] example = {{5,11,14,0}, {9,3,13, 7}, {2,8,10,12}, {4,1,15, 6}};
    
    // this constructor sets up the grid as initialGrid and displays it on the canvas
    // (plus it initialises the other instance variables)
    public FifteenPuzzle (int[][] initialGrid)
    {
        boolean[] contains = new boolean[16];
        
        grid = initialGrid;
        sc = new SimpleCanvas();
        sc.addMouseListener(this);
        
        for (int x = 0; x < initialGrid.length; x++){
            for (int y = 0; y < initialGrid[x].length; y++){
                int value = initialGrid[x][y];
                if (value == 0){
                    xspace = x;
                    yspace = y;
                }
                if (value <= 15 && value >= 0){
                    contains[value] = true;
                } else {
                    throw new IllegalArgumentException(value + " is not valid for a 4x4 game.");
                }
            }
        }
        
        for (boolean containsNumber : contains){
            if (!containsNumber){
                throw new IllegalArgumentException("The values 0 to 15 are not present");
            }
        }
        
        drawGrid();
    }
    
    // this constructor sets up the grid as goal, 
    // then it makes random moves to set up the puzzle and displays it on the canvas
    // (plus it initialises the other instance variables) 
    public FifteenPuzzle ()
    {
        
        grid = goal;
        sc = new SimpleCanvas();
        sc.addMouseListener(this);
        xspace = 3;
        yspace = 3;
        drawGrid();
        
        for (int i = 0; i<1000; i++){
            Random rand = new Random();
            int n = rand.nextInt(4);
            int x, y;
            switch (n){
                case 0:
                    x = xspace - 1;
                    y = yspace;
                    break;
                case 1:
                    x = xspace;
                    y = yspace + 1;
                    break;
                case 2:
                    x = xspace + 1;
                    y = yspace;
                    break;
                case 3:
                    x = xspace;
                    y = yspace - 1;
                    break;
                default:
                    x = -1;
                    y = -1;
                    break;
            }
            moveTile(x,y);
        }
        System.out.println("Begin!");
    }
    
    public void mouseClicked (MouseEvent e){
        int xpos = e.getX()/(tilesize*2);
        int ypos = e.getY()/(tilesize*2);
        moveTile(xpos, ypos);
        
        if (finished()){
            System.out.println("You won!");
            for (int x = 0; x< 4; x++){
                for (int y = 0; y< 4; y++){
                    drawTile(x,y, Color.magenta);
                    sc.repaint();
                }
            }
        }
    }
    
    public void mousePressed (MouseEvent e){}
    public void mouseReleased (MouseEvent e){}
    public void mouseEntered (MouseEvent e){}
    public void mouseExited (MouseEvent e){}
    
    // returns true iff x,y is adjacent to the space
    private boolean legalClick(int x, int y)
    {
        if (x > 3 || y > 3 || x < 0 || y < 0) return false;
        
        boolean horizontalLegal = ((x+1 == xspace) || (x-1 == xspace)) && (y == yspace);
        boolean verticalLegal = ((y+1 == yspace) || (y-1 == yspace)) && (x == xspace);
        return horizontalLegal || verticalLegal;
    }
    
    // returns true iff the puzzle is finished
    private boolean finished()
    {
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[i].length; j++){
                if (goal[i][j] != grid[i][j]){
                    return false;
                }
            }
        }
        return true;
    }
    
    // moves the tile at x,y into the space, if it is adjacent, and re-draws the grid; o/w do nothing 
    public void moveTile (int x, int y)
    {
        if (!legalClick(x,y)) return;
        
        int[][] newGrid = new int[4][4];
        
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[i].length; j++){
                newGrid[i][j] = grid[i][j];
            }
        }
        
        newGrid[xspace][yspace] = grid[x][y];
        newGrid[x][y] = 0;
        
        grid = newGrid;
        
        xspace = x;
        yspace = y;
        drawGrid();
        
    }
    
    // draws the current grid on the canvas
    private void drawGrid()
    {
        for (int x = 0; x< 4; x++){
            for (int y = 0; y< 4; y++){
                if (legalClick(x,y)){
                    drawTile(x,y, Color.cyan);
                } else {
                    drawTile(x,y, Color.green);
                }
                
            }
        }
        sc.repaint();
    }
    
    // draws the tile at x,y in colour c at the appropriate spot on the canvas
    private void drawTile(int x, int y, Color c)
    {
        String text;
        if (grid[x][y] == 0){
            text = "";
            x *= 100;
            y *= 100;
            sc.setForegroundColour(Color.black);
            sc.drawRectangle(x,y,x+100,y+100);
            sc.drawLine(x,y,x+100,y);
            sc.drawLine(x,y,x,y+100);
            sc.drawLine(x+100,y,x+100,y+100);
            sc.drawLine(x,y+100,x+100,y+100);
            
        } else{
            text = "" + grid[x][y];
            x *= 100;
            y *= 100;
            sc.setForegroundColour(c);
            sc.drawRectangle(x,y,x+100,y+100);
        }
        
        sc.setForegroundColour(Color.black);
        sc.drawLine(x,y,x+100,y);
        sc.drawLine(x,y,x,y+100);
        sc.drawLine(x+100,y,x+100,y+100);
        sc.drawLine(x,y+100,x+100,y+100);
        
        sc.drawString(text , x+50, y+50);
        
    }
}
