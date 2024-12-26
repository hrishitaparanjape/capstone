document.addEventListener('DOMContentLoaded', function () {
    const dreamDates = JSON.parse(document.getElementById('dream-dates').textContent).map(dream => new Date(dream.date));

    function calculateStreak(dates) {
        if (dates.length === 0) return 0;

        dates.sort((a, b) => a - b);
        let streak = 1;
        let currentStreak = 1;

        for (let i = 1; i < dates.length; i++) {
            const diffTime = Math.abs(dates[i] - dates[i - 1]);
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

            if (diffDays === 1) {
                currentStreak++;
            } else {
                currentStreak = 1;
            }

            if (currentStreak > streak) {
                streak = currentStreak;
            }
        }

        return streak;
    }

    const streak = calculateStreak(dreamDates);
    document.getElementById('streak').innerText = streak;
});