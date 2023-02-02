// SPDX-License-Identifier: MIT

pragma solidity 0.8.17;

interface IVestingPlatform {
    error VestingDoesNotExist();
    error VestingNotActive();
    error VestingInsufficentAmount();
    error WrongBeneficiary();
    error TransferFailed();
    error VestingAmountZero();
    error WrongEndTimestamp();
    error WrongVestingToken();

    struct VestingData {
        uint64 startTimestamp;
        uint64 endTimestamp;
        bool isActive;
        uint256 amount;
        uint256 amountClaimed;
    }

    /**
     * @notice Create a new vesting
     * @param beneficiary Address of the beneficiary
     * @param endTimestamp Timestamp when the vesting ends
     */
    function createVesting(address beneficiary, uint64 endTimestamp)
        external
        payable;

    /**
     * @notice Claim all vestings
     */
    function claimAllVestings() external;

    /**
     * @notice Get the amount of a vesting
     * @param amount Amount of the vesting
     * @param startTimestamp Timestamp when the vesting starts
     * @param endTimestamp Timestamp when the vesting ends
     * @param amountClaimed Amount already claimed
     * @return value Amount of the vesting
     */
    function vestingAmount(
        uint256 amount,
        uint64 startTimestamp,
        uint64 endTimestamp,
        uint256 amountClaimed
    ) external view returns (uint256 value);

    /**
     * @notice Claim a vesting and set the vesting to inactive if it has been claimed
     * @param index Index of the vesting
     */
    function claimVesting(uint256 index) external;

    /**
     * @notice Get all vestings of a beneficiary
     * @param beneficiary Address of the beneficiary
     * @return Array of vestings
     */
    function vestings(address beneficiary)
        external
        view
        returns (VestingData[] memory);

    /**
     * @notice Get a vesting of a beneficiary
     * @param beneficiary Address of the beneficiary
     * @param index Index of the vesting
     * @return Vesting
     */
    function vesting(address beneficiary, uint256 index)
        external
        view
        returns (VestingData memory);

    /**
     * @notice Get the amount of vestings of a beneficiary
     * @param beneficiary Address of the beneficiary
     * @return Amount of vestings
     */
    function vestingNumber(address beneficiary)
        external
        view
        returns (uint256);
}