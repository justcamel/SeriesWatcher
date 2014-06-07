import QtQuick 2.2
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1

ApplicationWindow {
    id: applicationWindow1
    visible: true
    width: 600; height: 900
    title: qsTr("Hello World")

    menuBar: MenuBar {
        Menu {
            title: qsTr("File")
            MenuItem {
                text: qsTr("Exit")
                onTriggered: Qt.quit();
            }
        }
    }

    ColumnLayout {
        anchors.rightMargin: 10
        anchors.leftMargin: 10
        anchors.bottomMargin: 10
        anchors.topMargin: 10
        spacing: 0

        SeriesBlock {
            seriesName: "Game of Thrones"
            releaseYear: "(2011-)"
            rating: "9.5 (102'329)"
            seasonNumber: "4"
            blockColor: "azure"
            imageSource: "qrc:icons/GoT.png"
        }

        EpisodeBlock {
            blockColor: "powderblue"
            episodeNumber: "6"
            episodeName: "The Laws of Gods and Men"
            hasReleased: true
        }

        EpisodeBlock {
            blockColor: "azure"
            episodeNumber: "7"
            episodeName: "Mockingbird"
            hasReleased: true
        }

        EpisodeBlock {
            blockColor: "powderblue"
            episodeNumber: "8"
            episodeName: "The Mountain and the Viper"
            releaseDate: "31/05/2014"
        }



        SeriesBlock {
            seriesName: "Fargo"
            releaseYear: "(2014-)"
            rating: "9.2 (22'206)"
            seasonNumber: "1"
            blockColor: "cornsilk"
            imageSource: "qrc:icons/fargo.png"
        }

        EpisodeBlock {
            blockColor: "darksalmon"
            episodeNumber: "3"
            episodeName: "A Muddy Road"
            hasReleased: true
        }

        EpisodeBlock {
            blockColor: "cornsilk"
            episodeNumber: "4"
            episodeName: "Eating the Blame"
            releaseDate: "05/06/2014"
        }


    }
}
