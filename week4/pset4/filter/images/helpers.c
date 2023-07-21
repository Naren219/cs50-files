#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gray_filt = round(image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue / 3)
            gray_filt = image[i][j].rgbtRed
            gray_filt = image[i][j].rgbtRed

        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue)
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue)
            int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue)
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
