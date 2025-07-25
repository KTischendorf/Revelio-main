document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM fully loaded and parsed');

    function parseCSV(csvData) {
        console.log('Parsing CSV data');
        const lines = csvData.trim().split('\n');
        const headers = lines.shift().split(',');
        const events = [];

        lines.forEach(line => {
            const data = line.split(',');
            const startDate = new Date(data[0]).toISOString().split('T')[0];
            const endDate = new Date(data[1]).toISOString().split('T')[0];

            // Create events for each role based on headers
            headers.slice(2).forEach((header, index) => {
                const person = data[index + 2];
                if (person) {
                    events.push({
                        title: `${person} (${header})`,
                        start: startDate,
                        end: endDate,
                        extendedProps: {
                            role: header,
                            columnIndex: index + 2 // Store the column index for ordering
                        }
                    });
                }
            });
        });

        console.log('Parsed events:', events);
        return events;
    }

    function generateColor(role) {
        // Base color
        const baseColor = [31, 119, 180]; // RGB for #1F77B4
        let hash = 0;
        for (let i = 0; i < role.length; i++) {
            hash = role.charCodeAt(i) + ((hash << 5) - hash);
        }
        const variation = Math.abs(hash) % 100; // Create a variation based on the hash
        const color = baseColor.map(c => Math.min(c + variation, 255)); // Adjust the base color
        return `rgb(${color.join(',')})`;
    }

    function initializeCalendar(events) {
        console.log('Initializing calendar');
        const calendarEl = document.getElementById('calendar');
        if (!calendarEl) {
            console.error('Calendar element not found');
            return;
        }
        console.log('Calendar element found:', calendarEl);

        // Assign colors to events based on their role
        events.forEach(event => {
            const color = generateColor(event.extendedProps.role);
            event.backgroundColor = color;
            event.borderColor = color;
        });

        const calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            events: events,
            height: 'auto', // Ensure the calendar has a height
            showNonCurrentDates: false, // Hide extra weeks
            fixedWeekCount: false, // Ensure the calendar only displays the necessary number of weeks
            eventOrder: (a, b) => {
                // Order events based on the column index
                return a.extendedProps.columnIndex - b.extendedProps.columnIndex;
            },
            hiddenDays: [] // Ensure no days are hidden
        });
        calendar.render();
        console.log('Calendar rendered with events:', events);
    }

    // Set the calendar title
    const titleEl = document.getElementById('calendar-title');
    if (titleEl) {
        titleEl.innerText = calendarTitle;
        console.log('Calendar title set:', calendarTitle);
    } else {
        console.error('Title element not found');
    }

    fetch(csvPath)
        .then(response => response.text())
        .then(csvData => {
            console.log('CSV data fetched');
            const events = parseCSV(csvData);
            initializeCalendar(events);
        })
        .catch(error => {
            console.error('Error fetching CSV data:', error);
        });
});
