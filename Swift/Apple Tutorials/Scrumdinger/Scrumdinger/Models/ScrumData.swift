//
/*
See LICENSE folder for this sample’s licensing information.
*/
//


import Foundation

class ScrumData: ObservableObject {
    // ObservableObject is a class-constrained protocol for connecting external model data to SwiftUI views.
    // It includes a publisher that emits before any of its @Published properties changes.
    
    // private computed property
    private static var documentsFolder: URL {
        // Adding the do-catch statement fixes possible compiler errors.
        do {
            return try FileManager.default.url(for: .documentDirectory,
                                               in: .userDomainMask,
                                               appropriateFor: nil,
                                               create: false)
        } catch {
            fatalError("Can't find documents directory.")
        }
    }
    private static var fileURL: URL {
        return documentsFolder.appendingPathComponent("scrums.data")
    }
    @Published var scrums: [DailyScrum] = []

    func load() {
        // Dispatch queues are first in, first out (FIFO) queues to which your application can submit tasks. Background tasks have the lowest priority of all tasks.
        DispatchQueue.global(qos: .background).async { [weak self] in
            // Use a weak reference to self inside the closure to avoid a retain cycle.
            // Data(contentsOf:options) can fail, so you use optional >>try?<< binding to unwrap Data.
            guard let data = try? Data(contentsOf: Self.fileURL) else {
                // You’ll use the #if DEBUG compiler directive to ensure that you have sample scrums to work with while you develop the app.
                #if DEBUG
                // Code inside the block is excluded from releases.
                DispatchQueue.main.async {
                    // Always perform UI updates on the main queue.
                    self?.scrums = DailyScrum.data
                }
                #endif
                return
            }
            // Because the try expression returns an optional upon failure, you use optional binding to capture the value of dailyScrums.
            guard let dailyScrums = try? JSONDecoder().decode([DailyScrum].self, from: data) else {
                fatalError("Can't decode saved scrum data.")
            }
            DispatchQueue.main.async {
                self?.scrums = dailyScrums
            }
        }
    }
    func save() {
        DispatchQueue.global(qos: .background).async { [weak self] in
            guard let scrums = self?.scrums else { fatalError("Self out of scope") }
            guard let data = try? JSONEncoder().encode(scrums) else { fatalError("Error encoding data") }
            do {
                let outfile = Self.fileURL
                try data.write(to: outfile)
                // write(to:options:) is a throwing function, so you handle any errors in a catch clause.
            } catch {
                fatalError("Can't write to file")
            }
        }
    }
}
