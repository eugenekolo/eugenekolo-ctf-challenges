import QtQuick 2.0
import QtQuick.Particles 2.0
import QtMultimedia 5.4
import QtGraphicalEffects 1.0

Rectangle {
    id: root
    width: 512
    height: 384
    color: "#1a1a1a"

    signal sendToQml(int resp)

    onSendToQml: {
        if (resp == 0) {
            hello.visible = false;
            shell.visible = false;
            password.visible = false;
            keyboard.visible = false;
            firework0.enabled = false;
            firework1.enabled = false;
            firework2.enabled = false;
            firework3.enabled = false;
            firework4.enabled = false;
            firework5.enabled = false;
            firework6.enabled = false;
            firework7.enabled = false;
            firework8.enabled = false;
            firework9.enabled = false;
            firework10.enabled = false;
            firework11.enabled = false;
            firework12.enabled = false;
            firework13.enabled = false;
            firework14.enabled = false;
            firework15.enabled = false;
            correct.visible = true;
            sparkle.visible = true;
            starsEmitter.enabled = true;
        } else {
            rotate.start();
        }
    }

    // === Play that funky music ===
    Audio {
        id: playMusic
        source: "qrc:/music.wav"
        autoPlay: true
    }


    // === Fill the sky up with stars baby ===
    ParticleSystem {
        id: stars
        anchors.fill: parent

        ImageParticle {
            groups: ["stars"]
            anchors.fill: parent
            source: "qrc:///particleresources/star.png"
        }

        Emitter {
            id: starsEmitter
            group: "stars"
            emitRate: 200
            lifeSpan: 1200
            size: 32
            sizeVariation: 8
            anchors.fill: parent
            enabled: false

        }

        Turbulence {
            anchors.fill: parent
            strength: 2
        }
    }

    ParticleSystem {
        id: correctFireworks
        anchors.fill: parent

        ImageParticle {
            id: rocketHead
            groups: ['rocket']
            source: "qrc:///particleresources/star.png"
            alpha: 0.3
        }

        Emitter {
            id: rocketEmitter
            anchors.bottom: parent.bottom
            width: parent.width; height: 40
            group: 'rocket'
            emitRate: 2
            //maximumEmitted: 4
            lifeSpan: 4800
            lifeSpanVariation: 400
            size: 32
            velocity: AngleDirection { angle: 270; magnitude: 150; magnitudeVariation: 10 }
        }

        ImageParticle {
            id: sparkle
            groups: ['sparkle']
            color: 'red'
            colorVariation: 0.6
            source: "qrc:///particleresources/star.png"
            alpha: 0.3
            visible: false
        }

        TrailEmitter {
           id: explosionEmitter
           anchors.fill: parent
           group: 'sparkle'
           follow: 'rocket'
           lifeSpan: 750
           emitRatePerParticle: 200
           size: 32
           velocity: AngleDirection { angle: -90; angleVariation: 180; magnitude: 50 }
        }

        TrailEmitter {
            id: explosion2Emitter
            anchors.fill: parent
            group: 'sparkle'
            follow: 'rocket'
            lifeSpan: 250
            emitRatePerParticle: 50
            size: 32
            velocity: AngleDirection { angle: 90; angleVariation: 15; magnitude: 400 }
        }
    }



    // === Greet the world ===
    Text {
        id: hello
        color: "steelblue"
        text: "It's dangerous to hack alone!\nTake this!"
        font.family: "Ubuntu Mono"
        font.bold: true
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        font.pointSize: 16
        anchors.centerIn: parent
        anchors.verticalCenterOffset: -140
   }

    // === Show the world ===
    Image {
       id: shell
       source: "qrc:/shell2.png"
       sourceSize.width: 48
       sourceSize.height: 48
       anchors.centerIn: parent
       anchors.verticalCenterOffset: -60
       RotationAnimation {
            id: rotate
            property: "rotation"
            target: shell
            from: 0
            to: 360
            duration: 1000
            direction: RotationAnimation.Clockwise
        }
   }


    // === First things first, first, rest in peace Uncle Phil ===
    Text {
        id: greetz
        text: "Greetz
        crowell | nhmood | 0xBU | shamu | kierk"
        font.family: "Ubuntu Mono"
        font.bold: true
        font.pointSize: 16
        visible: false

        LinearGradient {
            anchors.fill: parent
            source: parent
            start: Qt.point(0, 0)
            end: Qt.point(300, 0)
            gradient: Gradient {
                GradientStop { position: 0.15; color: "cyan" }
                GradientStop { position: 0.30; color: "steelblue" }
                GradientStop { position: 0.45; color: "cyan" }
                GradientStop { position: 0.60; color: "steelblue" }
                GradientStop { position: 0.75; color: "steelblue" }
                GradientStop { position: 0.90; color: "red" }
                GradientStop { position: 1.00; color: "cyan" }
            }
        }

        NumberAnimation on x {
            from: root.width
            to: -1*greetz.width
            loops: Animation.Infinite
            duration: 10000
        }
    }

    // === What's the password ? ===
    Text {
        id: password
        anchors.centerIn: parent
        anchors.verticalCenterOffset: 96
        color: "steelblue"
        font.family: "Ubuntu Mono"
        font.bold: true
        style: Text.Raised
        font.pointSize: 20
        text: "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        visible: true

   }

    // === Open sesame  ===
    Text {
        id: correct
        color: "steelblue"
        text: "Congratulations on\ncutie-keygen!"
        font.family: "Ubuntu Mono"
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        font.bold: true
        font.pointSize: 24
        anchors.centerIn: parent
        anchors.verticalCenterOffset: -100
        visible: false

   }


    // === Overly complicated fireworks off of letters ===
    ParticleSystem {
        id: fireworksSys
        ImageParticle {
             colorVariation: 0.6
             source: "qrc:///particleresources/star.png"
             alpha: 0
        }
   }

    // === Keyboard input ===
    Item {
        id: keyboard
        focus: true
        property var buffer: Array
        property var ptr: Number
        property var ready: Boolean
        property list<Emitter> fireworksList: [
            Emitter {
                property var name: String
                id: firework0
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework1
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework2
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
           },
            Emitter {
                property var name: String
                id: firework3
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework4
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework5
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework6
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework7
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework8
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework9
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework10
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework11
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework12
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework13
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework14
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            },
            Emitter {
                property var name: String
                id: firework15
                system: fireworksSys
                emitRate: 800
                lifeSpan: 750
                size: 32
                velocity: PointDirection {y:-17*4*2; xVariation: 6*6}
                acceleration: PointDirection {y: 17*2; xVariation: 6*6}
                enabled: false
            }
        ]

        function firework_on(pos) {
            var emitter = fireworksList[pos]
            emitter.x = 50 + pos*27
            emitter.y =  384/2 + 82;
            emitter.enabled = true;
        }

        function firework_off(pos) {
            var emitter = fireworksList[pos];
            emitter.enabled = false;
        }

        function pushChar(c) {
            if (ptr < 16) {
                buffer[ptr] = c;
                firework_on(ptr);

                ptr += 1;

                return true;
            }
            return false;
        }

        function popChar() {
            if (ptr >= 0) {
                buffer[ptr-1] = "_";
                firework_off(ptr-1);

                ptr -= 1;
                if (ptr === -1) {
                    ptr = 0;
                }

                return true;
            }
            return false
        }

        Component.onCompleted: {
            buffer = new Array(16);

            for (var i = 0; i < 16; i++) {
                buffer[i] = "_";
            }

            ptr = 0;
            ready = true;
        }

        Keys.onPressed: {
            if (!ready) {
                event.accepted = true;
                return;
            }

            if (event.key >= 0x21 && event.key <= 0x7e ) {
                pushChar(String.fromCharCode(event.key));
                var str = buffer.join(' ');
                password.text = str;
                event.accepted = true;
            } else if (event.key === Qt.Key_Return || event.key === Qt.Key_Enter) {
                var str = buffer.join(' ');
                if (str.match("G R E E T Z")) {
                    greetz.visible = true;
                }
                auth.receiveFromQml(str);

                event.accepted = true;
            } else if (event.key === Qt.Key_Backspace) {
                popChar();
                var str = buffer.join(' ');
                password.text = str;
                event.accepted = true;
            }
        }
    }

}

