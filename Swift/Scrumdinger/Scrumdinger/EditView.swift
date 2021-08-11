/*
 See LICENSE folder for this sample’s licensing information.
 */

import SwiftUI

struct EditView: View {
    // This View allow the user to access some editable features of the meeting
    
    // Because scrumData is now passed in during initialization, there's no need to use the @private property and DailyScrum.Data initialization.
    // no need of >>@Static private var scrumData: DailyScrum.Data = DailyScrum.Data()<<
    @Binding var scrumData: DailyScrum.Data
    // define the property using the @State wrapper because you need to mutate the property from within the view.
    /*
     SwiftUI observes @State properties and automatically redraws the view’s body when the property changes. This behavior ensures the UI stays up to
     date as the user manipulates the onscreen controls.
     */
    // Declare @State properties as private so they can be accessed only within the view in which you define them.
    // The newAttendee property will hold the attendee name the user enters.
    @State private var newAttendee = ""
    
    var body: some View {
        List {
            Section(header: Text("Meeting Info")) {
                // This textfield will hold the desired name for the meeting
                // It's default value will be "Title" but wil be able to change
                TextField("Title", text: $scrumData.title)
                HStack {
                    Slider(value: $scrumData.lengthInMinutes, in: 5...30, step: 1.0) {
                        // This Text view won’t appear on screen, but VoiceOver uses it to identify the purpose of the slider.
                        Text("Length")
                    }
                    .accessibilityValue(Text("\(Int(scrumData.lengthInMinutes)) minutes"))
                    Spacer()
                    Text("\(Int(scrumData.lengthInMinutes)) minutes")
                        .accessibilityHidden(true)
                }
                ColorPicker("Color", selection: $scrumData.color)
                    .accessibilityLabel(Text("Color picker"))
            }
            Section(header: Text("Attendees")) {
                ForEach(scrumData.attendees, id: \.self) { attendee in
                    Text(attendee)
                }
                .onDelete { indices in
                    scrumData.attendees.remove(atOffsets: indices)
                }
                HStack {
                    TextField("New Attendee", text: $newAttendee)
                    Button(action: {
                        withAnimation {
                            scrumData.attendees.append(newAttendee)
                            newAttendee = ""
                        }
                    }) {
                        Image(systemName: "plus.circle.fill")
                            .accessibilityLabel(Text("Add attendee"))
                    }
                    // Make unavailable to add attendees without text
                    .disabled(newAttendee.isEmpty)
                }
            }
        }
        .listStyle(InsetGroupedListStyle())
    }
}

struct EditView_Previews: PreviewProvider {
    static var previews: some View {
        EditView(scrumData: .constant(DailyScrum.data[0].data))
    }
}
