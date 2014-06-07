import QtQuick 2.2
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

Rectangle {
    property string seriesName
    property string releaseYear: "unknown"
    property string rating: "unknown"
    property string seasonNumber
    property string imageSource
    property color blockColor

    width: 550; height: 80
    anchors.left: parent.left
    anchors.leftMargin: 15

    color: blockColor

    Image {
        id: seriesIcon
        anchors.left: parent.left
//        width: 70; height: 70
        anchors.verticalCenter: parent.verticalCenter
        fillMode: Image.PreserveAspectCrop
        source: imageSource
        clip: true
    }

    Label {
        id: seriesNameLabel
        anchors.left: seriesIcon.right
        anchors.leftMargin: 10
        anchors.top: parent.top
        anchors.topMargin: 5
        font.pixelSize: 18
        text: seriesName
    }

    Label {
        text: releaseYear
        anchors.left: seriesNameLabel.right
        anchors.leftMargin: 3
        anchors.top: parent.top
        anchors.topMargin: 5
        font.pixelSize: 18
        font.italic: true
    }

    Label {
        id: ratingLabel
        anchors.left: seriesNameLabel.left
        anchors.leftMargin: 3
        anchors.top: seriesNameLabel.bottom
        anchors.topMargin: 5
        text: "IMDB: " + rating
    }

    Label {
        id: seasonNum
        anchors.left: seriesNameLabel.left
        anchors.leftMargin: 3
        anchors.top: ratingLabel.bottom
        anchors.topMargin: 2
        text: "Season " + seasonNumber
    }

}
