
                document.addEventListener("DOMContentLoaded", () => {
                  const counters = document.querySelectorAll('.counter');
                
                  counters.forEach(counter => {
                    const updateCount = () => {
                      const target = +counter.getAttribute('data-countto');
                      const duration = +counter.getAttribute('data-duration');
                      const increment = target / (duration / 10);
                      let count = 0;
                
                      const counterUpdate = setInterval(() => {
                        count += increment;
                        if (count < target) {
                          counter.textContent = Math.ceil(count);
                        } else {
                          counter.textContent = target;
                          clearInterval(counterUpdate);
                        }
                      }, 10);
                    };
                
                    updateCount();
                  });
                });
            