import QtQuick 2.2
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

Rectangle {
    property string episodeNumber
    property string episodeName
    property color blockColor
    property string releaseDate: "unknown"
    property bool hasReleased: false

    width: 550; height: 60

    anchors.left: parent.left
    anchors.leftMargin: 15

    color: blockColor

    Label {
        id: epNumLabel
        anchors.left: parent.left
        anchors.leftMargin: 10
        anchors.verticalCenter: parent.verticalCenter
        text: "Episode " + episodeNumber
        font.bold: true
        font.pixelSize: 16
    }

    Label {
        id: epNameLabel
        anchors.left: epNumLabel.right
        anchors.leftMargin: 10
        anchors.verticalCenter: parent.verticalCenter
        text: episodeName
        font.pixelSize: 16
    }

    Button {
        width: 120; height: 50
        opacity: hasReleased ? 1.0 : 0.5
        style: ButtonStyle {
            background: Rectangle {
                radius: 4
                gradient: Gradient {
                    GradientStop { position: 0 ; color: control.pressed ? "#ccc" : "#eee" }
                    GradientStop { position: 1 ; color: control.pressed ? "#aaa" : "#ccc" }
                }
            }
        }


        anchors.right: parent.right
        anchors.rightMargin: 10
        anchors.verticalCenter: parent.verticalCenter
        text: hasReleased ? "To desktop" : releaseDate
    }
}
