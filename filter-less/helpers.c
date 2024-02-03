#include "helpers.h"
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            BYTE gray_pixel = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3;
            image[i][j].rgbtBlue = gray_pixel;
            image[i][j].rgbtGreen = gray_pixel;
            image[i][j].rgbtRed = gray_pixel;
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
            // First, conver to grayscale
            BYTE gray_pixel = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3;

            // increase red and green values
            int SCALE = 20;
            BYTE rr = gray_pixel + (SCALE);
            BYTE gg = gray_pixel + (SCALE) / 2;


            // if "overflowing" - repair
            if (gg <= SCALE / 2 - 1)
                gg = 0xFF;
            if (rr <= SCALE - 1)
                rr = 0xFF;

            // set the new values for the pixel
            image[i][j].rgbtBlue = gray_pixel;
            image[i][j].rgbtGreen = gg;
            image[i][j].rgbtRed = rr;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < width; i++)
    {
        for (int j = 0, h_height = height / 2; j < h_height; j++)
        {
            RGBTRIPLE buffer = image[j][i];
            image[j][i] = image[height-j][i];
            image[height-j][i] = buffer;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
