#include "helpers.h"
#include <stdio.h>
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            BYTE gray_pixel = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0f);
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
            BYTE rr;
            BYTE gg;
            BYTE bb;

            int irr = round(0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            if (irr < 256)
                rr = irr;
            else
                rr = 255;

            int igg = round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            if (igg < 256)
                gg = igg;
            else
                gg = 255;


            int ibb = round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);
            if (ibb < 256)
                bb = ibb;
            else
                bb = 255;

            image[i][j].rgbtBlue = bb;
            image[i][j].rgbtGreen = gg;
            image[i][j].rgbtRed = rr;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, h_width = width/2; j < h_width; j++)
        {
            RGBTRIPLE buffer = image[i][j];
            image[i][j] = image[i][width-j-1];
            image[i][width-j-1] = buffer;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // make a copy of the image
    //otherwise bluring applies from the values of blurred pixels

    RGBTRIPLE copy[height][width];
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            copy[h][w] = image[h][w];
        }
    }

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
                    if (cur_x >= 0 && cur_y >= 0 && cur_x <= width && cur_y <= height)
                    {
                        count += 1;
                        arr_neig[count] = copy[cur_x][cur_y];
                    }
                }
            }

            // now calculate its values
            BYTE bb = 0x00;
            BYTE gg = 0x00;
            BYTE rr = 0x00;

            // workaround with int, to prevent overflow
            int colors[3] = {0,0,0};

            // add all the neighbor values
            for (int neig = 0; neig <= count; neig++)
            {
                colors[0] += arr_neig[neig].rgbtBlue;
                colors[1] += arr_neig[neig].rgbtGreen;
                colors[2] += arr_neig[neig].rgbtRed;
            }

            // prevent overflow
            for (int o = 0; o < 3; o++)
            {
                colors[o] = round(colors[o] / (float)(count+1));
                if (colors[o] > 255)
                    colors[o] = 255;
            }

            // convert to Bytes
            bb = colors[0];
            gg = colors[1];
            rr = colors[2];

            // write to image
            image[i][j].rgbtBlue = bb;
            image[i][j].rgbtGreen = gg;
            image[i][j].rgbtRed = rr;
        }
    }
    return;
}
