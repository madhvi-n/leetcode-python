class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        color = image[sr][sc] #changes will occur on this pixel only
        
        def mark_current_pixel(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            
            # only change the color if the pixel is of the source color, return if it's new color
            if image[row][col] == newColor or image[row][col] != color:
                return
            
            image[row][col] = newColor
            mark_current_pixel(row + 1, col)
            mark_current_pixel(row - 1, col)
            mark_current_pixel(row, col + 1)
            mark_current_pixel(row, col - 1)
        
        mark_current_pixel(sr, sc)
        return image