class ThreeSumSolver:
    """A class that solves 3Sum for portfolio optimization and AI feature selection."""
    
    def three_sum(self, nums):
        """
        Core Algorithm: Find all unique triplets that sum to zero.
        
        Time Complexity: O(n²)
        Space Complexity: O(1) excluding output
        
        Args:
            nums (list[int]): Array of integers
            
        Returns:
            list[list[int]]: All unique triplets that sum to zero
        """
        if len(nums) < 3:
            return []
        
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
    
    def find_risk_neutral_portfolios(self, asset_returns):
        """
        Business Use Case: Portfolio Risk Management
        
        Find combinations of 3 assets that create risk-neutral portfolios
        (total risk exposure = 0) for investment firms.
        
        Args:
            asset_returns (list[float]): Asset return percentages
            
        Returns:
            list: Risk-neutral portfolio combinations
        """
        # Scale to integers for computation
        scaled_returns = [int(r * 100) for r in asset_returns]
        triplets = self.three_sum(scaled_returns)
        
        # Convert back to percentages
        portfolios = []
        for triplet in triplets:
            portfolio = [r / 100.0 for r in triplet]
            portfolios.append({
                'assets': portfolio,
                'total_risk': sum(portfolio),
                'diversification': max(portfolio) - min(portfolio)
            })
        
        return portfolios
    
    def select_balanced_features(self, feature_scores):
        """
        AI Orchestration Use Case: Feature Selection for Bias Reduction
        
        Find combinations of 3 features that balance positive and negative
        bias to create fair AI models (total bias = 0).
        
        Args:
            feature_scores (list[float]): Feature bias scores
            
        Returns:
            list: Balanced feature combinations
        """
        # Scale to integers for computation
        scaled_scores = [int(score * 1000) for score in feature_scores]
        triplets = self.three_sum(scaled_scores)
        
        # Convert back to original scale
        feature_sets = []
        for triplet in triplets:
            features = [score / 1000.0 for score in triplet]
            feature_sets.append({
                'features': features,
                'total_bias': sum(features),
                'balance_score': 1.0 - abs(sum(features))  # Higher is better
            })
        
        return sorted(feature_sets, key=lambda x: x['balance_score'], reverse=True)

# --- Example Usage ---
def run_tests():
    """Demonstrate 3Sum algorithm with business and AI use cases."""
    
    solver = ThreeSumSolver()
    
    print("3Sum Problem: Portfolio Optimization & AI Feature Selection")
    print("-" * 55)
    
    # Core Algorithm Test
    print("\n1. Core 3Sum Algorithm:")
    nums = [-1, 0, 1, 2, -1, -4]
    result = solver.three_sum(nums)
    print(f"   Input: {nums}")
    print(f"   Triplets: {result}")
    
    # Business Use Case: Portfolio Management
    print("\n2. Business Use Case - Risk-Neutral Portfolios:")
    asset_returns = [-0.05, 0.02, -0.03, 0.08, -0.01, 0.04]
    portfolios = solver.find_risk_neutral_portfolios(asset_returns)
    
    print(f"   Asset Returns: {[f'{r:.2%}' for r in asset_returns]}")
    print(f"   Risk-Neutral Portfolios Found: {len(portfolios)}")
    
    for i, portfolio in enumerate(portfolios[:3]):  # Show top 3
        assets = [f'{r:.2%}' for r in portfolio['assets']]
        print(f"   Portfolio {i+1}: {assets} (Risk: {portfolio['total_risk']:.4f})")
    
    # AI Use Case: Feature Selection
    print("\n3. AI Use Case - Balanced Feature Selection:")
    feature_scores = [-0.7, 0.3, -0.1, 0.5, -0.2, 0.4]
    feature_sets = solver.select_balanced_features(feature_scores)
    
    print(f"   Feature Bias Scores: {feature_scores}")
    print(f"   Balanced Feature Sets Found: {len(feature_sets)}")
    
    for i, fs in enumerate(feature_sets[:3]):  # Show top 3
        features = [f'{f:.3f}' for f in fs['features']]
        print(f"   Set {i+1}: {features} (Bias: {fs['total_bias']:.6f})")

if __name__ == "__main__":
    run_tests()