/*
 See LICENSE folder for this sample’s licensing information.
 */

import SwiftUI

struct ScrumsView: View {
    @Binding var scrums: [DailyScrum]
    
    // You’ll observe this value and save user data when it becomes inactive.
    @Environment(\.scenePhase) private var scenePhase
    // The isPresented property controls the presentation of the EditView to create a new scrum.
    @State private var isPresented = false
    @State private var newScrumData = DailyScrum.Data()
    
    // You’ll provide the saveAction closure when instantiating ScrumsView.
    let saveAction: () -> Void
    
    var body: some View {
        List {
            ForEach(scrums) { scrum in
                // The destination presents a single view in the navigation hierarchy when a user interacts with the element.
                // Each row pushes to an individual destination.
                NavigationLink(destination: DetailView(scrum: binding(for: scrum))) {
                    CardView(scrum: scrum)
                }
                .listRowBackground(scrum.color)
            }
        }
        // Notice that the .navigationTitle modifier has been added to the List. The child view can affect the appearance of the NavigationView using modifiers.
        .navigationTitle("Daily Scrums")
        .navigationBarItems(trailing: Button(action: {
            isPresented = true
        }) {
            Image(systemName: "plus")
        })
        // A sheet presents a view similar to fullScreenCover, but it provides context by leaving the underlying view partially visible.
        .sheet(isPresented: $isPresented) {
            NavigationView {
                EditView(scrumData: $newScrumData)
                    .navigationBarItems(leading: Button("Dismiss") {
                        isPresented = false
                    }, trailing: Button("Add") {
                        let newScrum = DailyScrum(title: newScrumData.title, attendees: newScrumData.attendees,
                                                  lengthInMinutes: Int(newScrumData.lengthInMinutes), color: newScrumData.color)
                        scrums.append(newScrum)
                        isPresented = false
                    })
            }
        }
        // You can use onChange(of:perform:) to trigger actions when a specified value changes.
        .onChange(of: scenePhase) { phase in
            // A scene in the inactive phase no longer receives events and may be unavailable to the user.
            // Tip: Refer to ScenePhase for descriptions of each phase and instructions for triggering actions when the phase changes.
            if phase == .inactive { saveAction() }
        }
    }

    private func binding(for scrum: DailyScrum) -> Binding<DailyScrum> {
        guard let scrumIndex = scrums.firstIndex(where: { $0.id == scrum.id }) else {
            fatalError("Can't find scrum in array")
        }
        return $scrums[scrumIndex]
    }
}

struct ScrumsView_Previews: PreviewProvider {
    static var previews: some View {
        NavigationView {
            // pass an empty closure for the saveAction argument in the preview.
            ScrumsView(scrums: .constant(DailyScrum.data), saveAction: {})
        }
    }
}
