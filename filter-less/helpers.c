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

    // for every pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // variables for neighbors
            RGBTRIPLE arr_neig[9];
            int count = -1;

            // assemble its neighbors
            for (int k = 0; k < 3; k++)
            {
                for (int l = 0; l < 3; l++)
                {
                    int cur_x = i+k-1;
                    int cur_y = j+l-1;
                    // dont assemble if they are negative
                    if (cur_x >= 0 && cur_y >= 0)
                    {
                        count += 1;
                        arr_neig[count] = image[cur_x][cur_y];
                    }
                }
            }
            // now calculate its values
            // propably, this is gonna crash
            //b because of byte overflow
            BYTE bb = 0x00;
            BYTE gg = 0x00;
            BYTE rr = 0x00;
            for (int neig = 0; neig <= count; neig++)
            {
                if  (!(bb + (arr_neig[neig].rgbtBlue / count+1) >= 255))
                    bb += (arr_neig[neig].rgbtBlue / count+1);

                if  (!gg + (arr_neig[neig].rgbtBlue / count+1) >= 255)
                    gg += (arr_neig[neig].rgbtGreen / count+1);

                if  (!rr + (arr_neig[neig].rgbtBlue / count+1) >= 255)
                    rr += (arr_neig[neig].rgbtRed / count+1);
            }

            if (bb > 0xFF)
                bb = 0xFF;
            if (gg > 0xFF)
                gg = 0xFF;
            if (rr > 0xFF)
                rr = 0xFF;


            image[i][j].rgbtBlue = bb;
            image[i][j].rgbtGreen = gg;
            image[i][j].rgbtRed = rr;
        }
    }
    return;
}
