/*
See LICENSE folder for this sample’s licensing information.
*/

import SwiftUI

@main
struct ScrumdingerApp: App {
    
    @ObservedObject private var data = ScrumData()
    
    var body: some Scene {
        // If it would be an ipad or mac app it could have more than 1 View.
        // But because is an ios app the main scene for the app can have only 1 window
        WindowGroup {
            // Adding the NavigationView displays navigation elements, like title and bar buttons, on the canvas.
            NavigationView {
                ScrumsView(scrums: $data.scrums) {
                    // The app saves the user’s scrums when it becomes inactive.
                    data.save()
                }
            }
            .onAppear {
                data.load()
            }
        }
    }
}
// now the edit view
