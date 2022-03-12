#include "Image.h"

using namespace cv;
using std::to_string, std::string;
#include <iostream>

#define DESTINATION_FOLDER "../cone_detection/test_images/output/"

Image::Image(const string& imagePath) {
    this->identifier = std::stoi(imagePath.substr(imagePath.find_last_of('/') + 1));
    this->imagePath = imagePath + ".jpg";
    this->destinationFolder = DESTINATION_FOLDER + std::to_string(this->identifier);
    std::cout << this->destinationFolder << std::endl;
    this->originalImage = imread(this->imagePath);
}

Mat Image::createFixedSizeMatrix() const {
    return *new Mat(this->originalImage.rows, this->originalImage.cols, CV_8UC3, {0, 0, 0});
}

void Image::configureContourMatrices() {
    this->finalImage = this->originalImage.clone();
    this->mat.defaultContours = this->createFixedSizeMatrix();
    this->mat.approximatedContours = this->createFixedSizeMatrix();
    this->mat.convexContours = this->createFixedSizeMatrix();
    this->mat.coneContours = this->createFixedSizeMatrix();
}

std::vector<std::vector<Point>> Image::createFixedSizeVector() const {
    return *new std::vector<std::vector<Point>>(this->cont.contours.size());
}

void Image::configureContourVectors() {
    this->cont.filteredContours = this->createFixedSizeVector();
    this->cont.convexContours = this->createFixedSizeVector();
}

void Image::configureDestinationFolder() const {
    file::configureFolder(this->destinationFolder);
}

void Image::writeOnDisk(const string& fileName, const Mat& matrix) {
    imwrite(this->destinationFolder + "/" + fileName + ".jpg", matrix);
}

void Image::saveImagesOnDisk(const bool& saveStepByStep) {
    this->configureDestinationFolder();
    this->writeOnDisk("00original", this->originalImage);
    this->writeOnDisk("final", this->finalImage);

    if(saveStepByStep) {
        this->writeOnDisk("01hsv", this->mat.originalImageHsv);
        this->writeOnDisk("02mask", this->mat.mask);
        this->writeOnDisk("03blurred", this->mat.blurredImage);
        this->writeOnDisk("04canny", this->mat.cannyImage);
        this->writeOnDisk("05dilated", this->mat.dilatedImage);
        this->writeOnDisk("06eroded", this->mat.erodedImage);
        this->writeOnDisk("07default_contours", this->mat.defaultContours);
        this->writeOnDisk("08polygon", this->mat.defaultContours);
        this->writeOnDisk("09convex", this->mat.approximatedContours);
        this->writeOnDisk("10upwards", this->mat.coneContours);
    }
}

void Image::openImages(const bool& showStepByStep) const {
    imshow("original", this->originalImage);
    if(showStepByStep) {
        imshow("hsv", this->mat.originalImageHsv);
        imshow("mask", this->mat.mask);
        imshow("blurred", this->mat.blurredImage);
        imshow("canny", this->mat.cannyImage);
        imshow("dilated", this->mat.dilatedImage);
        imshow("eroded", this->mat.erodedImage);
        imshow("default contours", this->mat.defaultContours);
        imshow("polygon", this->mat.defaultContours);
        imshow("convex", this->mat.approximatedContours);
        imshow("upwards", this->mat.coneContours);
    }
    imshow("final", this->finalImage);
    waitKey();
}
