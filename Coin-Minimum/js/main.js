document.addEventListener('DOMContentLoaded', function() {
    // Data for charts
    const amounts = [734, 1000, 2001, 3003, 5000];
    
    // US Coins Data
    const usCoinsData = {
        'Memoized DP (Recursive)': [0.0016908645629882812, 0.002452373504638672, 0.004880189895629883, 0.00795602798461914, 0.008040904998779297],
        'Memoized DP (Iterative)': [0.001569986343383789, 0.0024051666259765625, 0.004127025604248047, 0.0053060054779052734, 0.007536172866821289],
        'Bottom-Up DP': [0.0005049705505371094, 0.0007419586181640625, 0.0013308525085449219, 0.0015468597412109375, 0.002366304397583008],
        'Greedy': [5.7220458984375e-06, 5.0067901611328125e-06, 1.0013580322265625e-05, 4.0531158447265625e-06, 3.0994415283203125e-06]
    };
    
    // Standard Coins Data
    const standardCoinsData = {
        'Memoized DP (Recursive)': [0.0022039413452148438, 0.002905130386352539, 0.004912137985229492, 0.006478786468505859, 0.008990049362182617],
        'Memoized DP (Iterative)': [0.002128124237060547, 0.0025298595428466797, 0.0029370784759521484, 0.005897045135498047, 0.008638143539428711],
        'Bottom-Up DP': [0.0006780624389648438, 0.0008089542388916016, 0.001461029052734375, 0.0017991065979003906, 0.002565145492553711],
        'Greedy': [1.0967254638671875e-05, 4.76837158203125e-06, 4.76837158203125e-06, 4.0531158447265625e-06, 6.198883056640625e-06]
    };
    
    // Prime Coins Data
    const primeCoinsData = {
        'Memoized DP (Recursive)': [0.003110170364379883, 0.004837989807128906, 0.01987481117248535, 0.00556492805480957, 0.009869098663330078],
        'Memoized DP (Iterative)': [0.00205230712890625, 0.0018630027770996094, 0.0038251876831054688, 0.005759000778198242, 0.009532928466796875],
        'Bottom-Up DP': [0.0003991127014160156, 0.0005507469177246094, 0.0011668205261230469, 0.0016939640045166016, 0.0030050277709960938],
        'Greedy': [6.198883056640625e-06, 4.0531158447265625e-06, 7.867813110351562e-06, 7.867813110351562e-06, 1.2874603271484375e-05]
    };
    
    // Binary Coins Data
    const binaryCoinsData = {
        'Memoized DP (Recursive)': [0.0013279914855957031, 0.0017228126525878906, 0.00526118278503418, 0.007047176361083984, 0.010161161422729492],
        'Memoized DP (Iterative)': [0.0011188983917236328, 0.001870870590209961, 0.005318880081176758, 0.0066950321197509766, 0.009437084197998047],
        'Bottom-Up DP': [0.0003769397735595703, 0.0005950927734375, 0.0017330646514892578, 0.0020329952239990234, 0.002872943878173828],
        'Greedy': [4.76837158203125e-06, 1.6689300537109375e-06, 5.7220458984375e-06, 4.0531158447265625e-06, 5.9604644775390625e-06]
    };

    // Create charts
    createRuntimeChart('usCoinsChart', 'US Coins Runtime Comparison', amounts, usCoinsData);
    createRuntimeChart('standardCoinsChart', 'Standard Coins Runtime Comparison', amounts, standardCoinsData);
    createRuntimeChart('primeCoinsChart', 'Prime Coins Runtime Comparison', amounts, primeCoinsData);
    createRuntimeChart('binaryCoinsChart', 'Binary Coins Runtime Comparison', amounts, binaryCoinsData);
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});

// Add at the end of your existing JavaScript

// Back to top button functionality
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  const backToTopBtn = document.getElementById("backToTopBtn");
  
  if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
    backToTopBtn.style.display = "block";
  } else {
    backToTopBtn.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
document.getElementById("backToTopBtn").addEventListener("click", function() {
  // For smooth scrolling
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});
